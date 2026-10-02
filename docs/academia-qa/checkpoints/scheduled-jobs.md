# Checkpoint `scheduled-jobs`

## Antes

O espelho não cumpre esta fatia.

## Depois

Há Quartz ou dependência quartz e um @Scheduled. README explica a diferença. Há menção a idempotência do job.

## Como verificar

`scripts/academy/validate-checkpoint.ps1 -Checkpoint scheduled-jobs`

## Honesto

Se falhar, o capstone lista a dívida. Não apague o validador.
