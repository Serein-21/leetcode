# Last updated: 1/2/2026, 12:17:56 PM
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        length = len(flowerbed)
        for i in range(length):
            can_plant = flowerbed[i] == 0
            if i > 0:
                can_plant = can_plant and flowerbed[i - 1] == 0
            if i < length - 1:
                can_plant = can_plant and flowerbed[i + 1] == 0

            if can_plant:
                flowerbed[i] = 1  # Plant the flower
                count += 1
                if count >= n:
                    return True
        return count >= n