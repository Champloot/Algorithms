import math

class RMQDecomposition:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)
        self.block_size = int(math.sqrt(self.n)) + 1
        self.min_blocks = []
        # Вычисляем минимумы для каждого блока
        for i in range(0, self.n, self.block_size):
            block = self.arr[i:i+self.block_size]
            self.min_blocks.append(min(block))
    
    def query(self, l, r):
        if l < 0 or r >= self.n or l > r:
            raise ValueError("Некорректный диапазон")
        min_val = float('inf')
        start_block = l // self.block_size
        end_block = r // self.block_size
        
        if start_block == end_block:
            # Все элементы в одном блоке
            for i in range(l, r + 1):
                if self.arr[i] < min_val:
                    min_val = self.arr[i]
        else:
            # Обрабатываем хвост начального блока
            for i in range(l, (start_block + 1) * self.block_size):
                if i >= self.n:
                    break
                if self.arr[i] < min_val:
                    min_val = self.arr[i]
            # Обрабатываем полные блоки
            for b in range(start_block + 1, end_block):
                if b >= len(self.min_blocks):
                    break
                if self.min_blocks[b] < min_val:
                    min_val = self.min_blocks[b]
            # Обрабатываем начало конечного блока
            for i in range(end_block * self.block_size, r + 1):
                if i >= self.n:
                    break
                if self.arr[i] < min_val:
                    min_val = self.arr[i]
        return min_val

# Пример использования
arr = [1, 3, 2, 5, 4, 6]
rmq = RMQDecomposition(arr)

print(rmq.query(0, 5))  # 1
print(rmq.query(2, 4))  # 2
print(rmq.query(3, 5))  # 4
