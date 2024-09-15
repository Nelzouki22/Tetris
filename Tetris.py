import pygame
import random

pygame.init()

# إعدادات الشاشة
screen_width, screen_height = 800, 700  # عرض وارتفاع الشاشة
play_width, play_height = 300, 600  # مساحة اللعب (شبكة 10x20)
block_size = 30  # حجم كل بلوك

top_left_x = (screen_width - play_width) // 2  # تحديد إحداثيات الزاوية اليسرى العلوية لمساحة اللعب
top_left_y = screen_height - play_height - 50

# تعريف الأشكال
S = [['.....', '.....', '..00.', '.00..', '.....'], ['.....', '..0..', '..00.', '...0.', '.....']]
Z = [['.....', '.....', '.00..', '..00.', '.....'], ['.....', '..0..', '.00..', '.0...', '.....']]
I = [['..0..', '..0..', '..0..', '..0..', '.....'], ['.....', '0000.', '.....', '.....', '.....']]
O = [['.....', '.....', '.00..', '.00..', '.....']]
J = [['.....', '.0...', '.000.', '.....', '.....'], ['.....', '..00.', '..0..', '..0..', '.....']]
L = [['.....', '...0.', '.000.', '.....', '.....'], ['.....', '..0..', '..0..', '..00.', '.....']]
T = [['.....', '..0..', '.000.', '.....', '.....'], ['.....', '..0..', '..00.', '..0..', '.....']]

shapes = [S, Z, I, O, J, L, T]  # قائمة تحتوي على الأشكال
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]  # ألوان الأشكال

# كلاس القطعة (Piece)
class Piece:
    def __init__(self, x, y, shape):
        self.x = x  # إحداثيات X
        self.y = y  # إحداثيات Y
        self.shape = shape  # الشكل الحالي
        self.color = shape_colors[shapes.index(shape)]  # اللون المناسب للشكل
        self.rotation = 0  # تدوير الشكل (بدءًا من 0)

# إنشاء الشبكة
def create_grid(locked_positions={}):
    # الشبكة عبارة عن قائمة تحتوي على ألوان مربعات اللعبة
    grid = [[(0, 0, 0) for _ in range(10)] for _ in range(20)]  # 20 صف و10 أعمدة (اللون الأسود في البداية)
    # ملء الشبكة بالمربعات المغلقة (القطع الثابتة)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if (x, y) in locked_positions:
                grid[y][x] = locked_positions[(x, y)]  # تحديد اللون في المربعات المغلقة
    return grid

# رسم الشبكة
def draw_grid(surface):
    # رسم الخطوط الأفقية والرأسية للشبكة
    for i in range(play_height // block_size):
        pygame.draw.line(surface, (128, 128, 128), (top_left_x, top_left_y + i * block_size), (top_left_x + play_width, top_left_y + i * block_size))
    for j in range(play_width // block_size):
        pygame.draw.line(surface, (128, 128, 128), (top_left_x + j * block_size, top_left_y), (top_left_x + j * block_size, top_left_y + play_height))

# رسم نافذة اللعبة
def draw_window(surface, grid):
    surface.fill((0, 0, 0))  # ملء الخلفية باللون الأسود
    # رسم المربعات حسب ألوانها في الشبكة
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            pygame.draw.rect(surface, grid[y][x], (top_left_x + x * block_size, top_left_y + y * block_size, block_size, block_size), 0)
    draw_grid(surface)  # رسم خطوط الشبكة
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)  # إطار حول مساحة اللعب

# اختيار شكل عشوائي
def get_shape():
    return Piece(5, 0, random.choice(shapes))  # إرجاع قطعة جديدة عشوائية تبدأ من أعلى الشاشة

# الحلقة الرئيسية للعبة
def main():
    locked_positions = {}  # المواقع المغلقة (التي تحتوي على قطع ثابتة)
    grid = create_grid()  # إنشاء الشبكة
    current_piece = get_shape()  # القطعة الحالية
    next_piece = get_shape()  # القطعة التالية
    clock = pygame.time.Clock()  # ضبط وقت اللعبة
    fall_time = 0  # وقت سقوط القطعة
    fall_speed = 0.27  # سرعة سقوط القطعة
    run = True  # متغير لاستمرار اللعبة

    while run:
        grid = create_grid(locked_positions)  # تحديث الشبكة بالمربعات المغلقة
        fall_time += clock.get_rawtime()  # حساب الوقت المنقضي
        clock.tick()  # تحديث الساعة

        # إسقاط القطعة عند انقضاء الوقت المحدد
        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1  # تحريك القطعة للأسفل
            if not valid_space(current_piece, grid) and current_piece.y > 0:
                current_piece.y -= 1  # إرجاع القطعة لموقعها السابق عند الاصطدام
                add_to_locked(locked_positions, current_piece)  # إضافة القطعة إلى المواقع المغلقة
                current_piece = next_piece  # تحديث القطعة الحالية
                next_piece = get_shape()  # تحديد القطعة التالية
                if check_lost(locked_positions):
                    run = False  # إنهاء اللعبة عند الخسارة

        draw_window(win, grid)  # رسم النافذة والشبكة
        pygame.display.update()  # تحديث الشاشة

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False  # إنهاء اللعبة عند إغلاق النافذة

    pygame.quit()  # إغلاق نافذة اللعبة عند الانتهاء

# التحقق من صحة المساحة المتاحة لوضع القطعة
def valid_space(piece, grid):
    accepted_pos = [[(x, y) for x in range(10) if grid[y][x] == (0, 0, 0)] for y in range(20)]  # المواقع الفارغة
    accepted_pos = [x for sub in accepted_pos for x in sub]
    formatted = convert_shape_format(piece)

    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:  # إذا كانت القطعة ضمن الشاشة
                return False
    return True

# إضافة القطعة إلى المواقع المغلقة
def add_to_locked(locked_positions, piece):
    for pos in convert_shape_format(piece):
        p = (pos[0], pos[1])
        locked_positions[p] = piece.color  # تحديد اللون في الموقع المغلق

# تحويل شكل القطعة إلى تنسيق إحداثيات
def convert_shape_format(piece):
    positions = []
    format = piece.shape[piece.rotation % len(piece.shape)]  # الحصول على الشكل بعد التدوير
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((piece.x + j, piece.y + i))  # تحويل التنسيق إلى إحداثيات
    return positions

# التحقق من الخسارة
def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:  # إذا كانت أي قطعة فوق الشاشة
            return True
    return False

win = pygame.display.set_mode((screen_width, screen_height))  # إعداد نافذة اللعبة
pygame.display.set_caption("Tetris")  # عنوان النافذة
main()  # تشغيل اللعبة

