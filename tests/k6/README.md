# k6 — baseline local

Mede o POST do pedido no oráculo. Não é capacidade de produção.

No host (k6 instalado na máquina):

```bash
k6 run tests/k6/pedido-baseline.js
```

Dentro do Docker, use a rede do Compose. `host.docker.internal` neste lab WSL não alcança a porta publicada.

```bash
docker run --rm --network infra_default \
  -v "$PWD/tests/k6:/scripts" \
  -e BASE_URL=http://api-gateway:11001 \
  grafana/k6:0.57.0 run /scripts/pedido-baseline.js
```

Thresholds largos de propósito (p95 < 5s, erro < 20%). Se falhar, anote o número. Não afrouxe o arquivo só para ficar verde sem registrar o fato.

Não aponte `BASE_URL` para máquina que não é sua.
