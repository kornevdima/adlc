import { expect, test } from 'vitest';
import { createOrder } from './orders.js';

test('rejects non-positive totals', () => {
  expect(() => createOrder('o1', 0)).toThrow();
});
