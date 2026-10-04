export function createOrder(id: string, total: number) {
  if (total <= 0) throw new Error('total must be positive');
  return { id, total, status: 'created' as const };
}
