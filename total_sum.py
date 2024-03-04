def total_sum(root):
    if root is None:
        return 0
    
    # Рекурсивно обчислюємо суму значень у лівому піддереві
    left_sum = total_sum(root.left)
    
	# Рекурсивно обчислюємо суму значень у правому піддеревах
    right_sum = total_sum(root.right)
    
    # Сума всіх значень
    return root.val + left_sum + right_sum