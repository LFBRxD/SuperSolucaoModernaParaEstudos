package com.studyshop.gateway.security;

import java.util.List;
import java.util.Map;
import java.util.Optional;
import org.springframework.boot.autoconfigure.condition.ConditionalOnProperty;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;

@Component
@ConditionalOnProperty(name = "studyshop.auth.mode", havingValue = "local", matchIfMissing = true)
public class LocalUserStore {

    public record LocalUser(String username, String passwordHash, List<String> roles) {
    }

    private final Map<String, LocalUser> users;

    public LocalUserStore(PasswordEncoder passwordEncoder) {
        this.users = Map.of(
                "qa", new LocalUser("qa", passwordEncoder.encode("qa123"), List.of("USER")),
                "admin", new LocalUser("admin", passwordEncoder.encode("admin123"), List.of("USER", "ADMIN"))
        );
    }

    public Optional<LocalUser> find(String username) {
        return Optional.ofNullable(users.get(username));
    }
}
