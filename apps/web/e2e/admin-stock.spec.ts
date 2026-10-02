import { expect, test } from '@playwright/test'
import { login } from './helpers'

test('admin salva estoque', async ({ page }) => {
  await login(page, 'admin', 'admin123')
  await page.getByTestId('nav-admin-stock').click()
  await expect(page.getByTestId('admin-stock-title')).toBeVisible()
  await page.getByTestId('input-stock-prod-notebook').fill('10')
  await page.getByTestId('btn-save-stock-prod-notebook').click()
  await expect(page.getByTestId('stock-ok')).toBeVisible()
})
