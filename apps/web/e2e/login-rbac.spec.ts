import { expect, test } from '@playwright/test'
import { login } from './helpers'

test('qa nao ve estoque e admin ve', async ({ page }) => {
  await login(page, 'qa', 'qa123')
  await expect(page.getByTestId('nav-admin-stock')).toHaveCount(0)
  await page.getByTestId('btn-logout').click()
  await login(page, 'admin', 'admin123')
  await expect(page.getByTestId('nav-admin-stock')).toBeVisible()
})
