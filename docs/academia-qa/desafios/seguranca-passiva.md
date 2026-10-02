# Checklist passivo (localhost)

Marque achado ou não, com arquivo. Não escaneie rede que não é sua.

- [ ] `GET` em `http://localhost:11007/api/notifications` sem token responde 200
- [ ] CORS do gateway permite origem ampla (`CorsConfig`)
- [ ] Kafka no Compose está `PLAINTEXT`
- [ ] Mongo no Compose não pede senha
- [ ] `docs/seguranca.md` diz que isso é lab
- [ ] UI esconder o menu não impede PUT (403 com token de qa)
- [ ] Segredo JWT do lab está no Compose e não deve ir para outro ambiente

Correção esperada no espelho: não copiar a porta aberta sem auth.
