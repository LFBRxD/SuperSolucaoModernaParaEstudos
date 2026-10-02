import { expect, type APIRequestContext, type Page } from '@playwright/test'

const api = process.env.E2E_API_URL ?? 'http://localhost:11001'

export async function login(page: Page, username: string, password: string) {
  await page.goto('/login')
  await page.getByTestId('input-username').fill(username)
  await page.getByTestId('input-password').fill(password)
  await page.getByTestId('btn-login').click()
  await page.waitForURL((url) => !url.pathname.includes('/login'))
  await expect(page.getByTestId('catalog-title')).toBeVisible()
}

export async function token(request: APIRequestContext, username: string, password: string) {
  const res = await request.post(`${api}/api/auth/login`, {
    data: { username, password },
  })
  expect(res.ok()).toBeTruthy()
  const body = await res.json()
  return body.accessToken as string
}

export async function setStock(request: APIRequestContext, productId: string, quantity: number) {
  const admin = await token(request, 'admin', 'admin123')
  const res = await request.put(`${api}/api/products/${productId}/stock`, {
    headers: { Authorization: `Bearer ${admin}` },
    data: { quantity },
  })
  expect(res.ok()).toBeTruthy()
}

export async function createViaUi(page: Page, productId: string, times: number, forceFail: boolean) {
  for (let i = 0; i < times; i++) {
    await page.getByTestId(`btn-add-${productId}`).click()
  }
  await page.getByTestId('input-customer-email').fill('e2e@studyshop.local')
  if (forceFail) {
    await page.getByTestId('chk-force-payment-failure').check()
  }
  await page.getByTestId('btn-create-order').click()
  await expect(page.getByTestId('order-created-alert')).toBeVisible()
  await page.getByTestId('link-created-order').click()
  await expect(page.getByTestId('order-status')).toHaveText(/CONFIRMED|CANCELLED/, { timeout: 60_000 })
  return page.getByTestId('order-status')
}
