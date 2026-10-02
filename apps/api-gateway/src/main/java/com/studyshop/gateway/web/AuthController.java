package com.studyshop.gateway.web;

import com.studyshop.gateway.security.JwtService;
import com.studyshop.gateway.security.LocalUserStore;
import java.util.List;
import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.http.HttpStatus;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.server.ResponseStatusException;

@RestController
@RequestMapping("/api/auth")
@ConditionalOnProperty(name = "studyshop.auth.mode", havingValue = "local", matchIfMissing = true)
public class AuthController {

    public record LoginRequest(String username, String password) {
    }

    public record TokenResponse(String accessToken, String tokenType, long expiresIn, List<String> roles) {
    }

    private final LocalUserStore userStore;
    private final PasswordEncoder passwordEncoder;
    private final JwtService jwtService;

    public AuthController(LocalUserStore userStore, PasswordEncoder passwordEncoder, JwtService jwtService) {
        this.userStore = userStore;
        this.passwordEncoder = passwordEncoder;
        this.jwtService = jwtService;
    }

    @PostMapping("/login")
    public TokenResponse login(@RequestBody LoginRequest body) {
        if (body == null || body.username() == null || body.password() == null) {
            throw new ResponseStatusException(HttpStatus.BAD_REQUEST, "username e password são obrigatórios");
        }
        var user = userStore.find(body.username())
                .filter(u -> passwordEncoder.matches(body.password(), u.passwordHash()))
                .orElseThrow(() -> new ResponseStatusException(HttpStatus.UNAUTHORIZED, "Credenciais inválidas"));
        String token = jwtService.createToken(user.username(), user.roles());
        return new TokenResponse(token, "Bearer", jwtService.expirationSeconds(), user.roles());
    }
}
