import { expect, test } from '@playwright/test'
import { createViaUi, login } from './helpers'

test('falha de pagamento cancela', async ({ page }) => {
  await login(page, 'qa', 'qa123')
  const status = await createViaUi(page, 'prod-teclado', 1, true)
  await expect(status).toHaveText('CANCELLED')
  await expect(page.getByTestId('order-status-reason')).not.toBeEmpty()
})
