import AxeBuilder from '@axe-core/playwright'
import { expect, test } from '@playwright/test'
import { login } from './helpers'

test('login nao tem violacao critica do axe', async ({ page }) => {
  await page.goto('/login')
  const results = await new AxeBuilder({ page }).analyze()
  expect(results.violations.filter((v) => v.impact === 'critical')).toEqual([])
})

test('catalogo autenticado nao tem violacao critica do axe', async ({ page }) => {
  await login(page, 'qa', 'qa123')
  const results = await new AxeBuilder({ page }).analyze()
  expect(results.violations.filter((v) => v.impact === 'critical')).toEqual([])
})
