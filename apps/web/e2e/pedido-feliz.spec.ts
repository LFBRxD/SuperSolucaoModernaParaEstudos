import { expect, test } from '@playwright/test'
import { createViaUi, login } from './helpers'

test('pedido feliz chega em CONFIRMED', async ({ page }) => {
  await login(page, 'qa', 'qa123')
  const status = await createViaUi(page, 'prod-headset', 1, false)
  await expect(status).toHaveText('CONFIRMED')
  await expect(page.getByTestId('order-id')).not.toBeEmpty()
})
