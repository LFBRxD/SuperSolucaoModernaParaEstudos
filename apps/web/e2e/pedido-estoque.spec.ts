import { expect, test } from '@playwright/test'
import { createViaUi, login, setStock } from './helpers'

test('quantidade acima do estoque cancela', async ({ page, request }) => {
  await setStock(request, 'prod-raro', 1)
  await login(page, 'qa', 'qa123')
  const status = await createViaUi(page, 'prod-raro', 2, false)
  await expect(status).toHaveText('CANCELLED')
})
