import http from 'k6/http'
import { check, sleep } from 'k6'

export const options = {
  vus: 1,
  iterations: 5,
  thresholds: {
    http_req_failed: ['rate<0.2'],
    http_req_duration: ['p(95)<5000'],
  },
}

const base = __ENV.BASE_URL || 'http://localhost:11001'

export default function () {
  const login = http.post(
    `${base}/api/auth/login`,
    JSON.stringify({ username: 'qa', password: 'qa123' }),
    { headers: { 'Content-Type': 'application/json' } },
  )
  check(login, { 'login 200': (r) => r.status === 200 })
  if (login.status !== 200) {
    sleep(1)
    return
  }
  const token = login.json('accessToken')
  const order = http.post(
    `${base}/api/orders`,
    JSON.stringify({
      customerEmail: 'k6@studyshop.local',
      forcePaymentFailure: false,
      items: [{ productId: 'prod-headset', quantity: 1 }],
    }),
    {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`,
      },
    },
  )
  check(order, { 'pedido aceito': (r) => r.status === 200 })
  sleep(1)
}
