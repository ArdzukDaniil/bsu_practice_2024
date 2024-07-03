N = int(input().strip())
blocks = []
for _ in range(N):
    blocks.append(int(input().strip()))

previous_hash = 0
error_block_index = -1

for i in range(N):
    bn = blocks[i]
    h_n = bn % 256
    r_n = (bn // 256) % 256
    m_n = (bn // 256 ** 2) % 256

    if h_n >= 100:
        error_block_index = i
        break

    calculated_hash = (37 * (m_n + r_n + previous_hash)) % 256

    if h_n != calculated_hash:
        error_block_index = i
        break

    previous_hash = h_n

print(error_block_index)
