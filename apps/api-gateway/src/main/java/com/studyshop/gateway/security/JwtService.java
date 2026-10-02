package com.studyshop.gateway.security;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.security.Keys;
import java.nio.charset.StandardCharsets;
import java.time.Instant;
import java.util.Collection;
import java.util.Date;
import java.util.List;
import javax.crypto.SecretKey;
import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.stereotype.Service;

@Service
@ConditionalOnProperty(name = "studyshop.auth.mode", havingValue = "local", matchIfMissing = true)
public class JwtService {

    private final JwtProperties properties;
    private final SecretKey key;

    public JwtService(JwtProperties properties) {
        this.properties = properties;
        byte[] secretBytes = properties.getSecret().getBytes(StandardCharsets.UTF_8);
        if (secretBytes.length < 32) {
            throw new IllegalStateException("studyshop.jwt.secret deve ter ao menos 32 bytes (HS256)");
        }
        this.key = Keys.hmacShaKeyFor(secretBytes);
    }

    public String createToken(String username, Collection<String> roles) {
        Instant now = Instant.now();
        Instant exp = now.plusSeconds(properties.getExpirationMinutes() * 60);
        return Jwts.builder()
                .issuer(properties.getIssuer())
                .subject(username)
                .claim("roles", List.copyOf(roles))
                .issuedAt(Date.from(now))
                .expiration(Date.from(exp))
                .signWith(key)
                .compact();
    }

    public Claims parse(String token) {
        return Jwts.parser()
                .verifyWith(key)
                .requireIssuer(properties.getIssuer())
                .build()
                .parseSignedClaims(token)
                .getPayload();
    }

    public long expirationSeconds() {
        return properties.getExpirationMinutes() * 60;
    }
}
