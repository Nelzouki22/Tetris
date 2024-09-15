# Tetris
لعبة تيتريس باستخدام بايثون و Pygame
وصف المشروع:
هذا المشروع عبارة عن لعبة تيتريس تم تطويرها باستخدام Python و Pygame. اللعبة تحتوي على الميزات الكلاسيكية للتيتريس مثل الأشكال المتساقطة، والتحكم في الشبكة، وزيادة الصعوبة مع التقدم في اللعبة.

الميزات:
أشكال تيتريس الكلاسيكية: تشمل الأشكال السبعة القياسية لتيتريس (S، Z، I، O، J، L، T) بألوان مميزة.
اللعب الديناميكي: تزداد سرعة اللعبة مع تقدم اللاعب، مما يجعلها أكثر تحديًا.
تحديثات في الوقت الحقيقي: يتم تحديث نافذة اللعبة في الوقت الفعلي، مع عرض الشكل الحالي والقطع الثابتة.
كشف التصادم: التأكد من توقف الأشكال عندما تصل إلى القاع أو تصطدم بقطع أخرى.
شروط نهاية اللعبة: اللعبة تنتهي عندما لا تكون هناك مساحات متاحة، مما يشير إلى انتهاء اللعبة.
ما ستتعلمه:
معالجة القوائم متعددة الأبعاد لشبكة اللعبة.
كيفية استخدام Pygame لإنشاء نوافذ تفاعلية وإدارة الرسومات.
الحلقات البرمجية الأساسية، التحديثات في الوقت الفعلي، والتعامل مع الأحداث.
كشف التصادم والميكانيكيات القائمة على الشبكة.
طريقة منظمة لإدارة القطع المتساقطة، التدوير، وتحديد المواقع المغلقة.
كيفية التشغيل:
قم باستنساخ هذا المستودع.
تأكد من تثبيت Python 3.x ومكتبة Pygame.
قم بتشغيل ملف main.py لبدء اللعبة.
bash
Copy code
git clone <your-repo-url>
cd <your-repo-directory>
python main.py
التحسينات المستقبلية:
إضافة نظام النقاط وحفظ أفضل النتائج.
تنفيذ قائمة بداية وشاشة نهاية.
مستويات صعوبة متقدمة وزيادة تدريجية في السرعة.
Tetris Game using Python and Pygame
Project Description:
This project is a Tetris game built using Python and Pygame. It includes classic Tetris features such as falling shapes, grid-based gameplay, and increasing difficulty as the game progresses.

Features:
Classic Tetris Shapes: Includes the seven standard Tetris shapes (S, Z, I, O, J, L, T) with unique colors.
Dynamic Gameplay: The game speed increases as the player progresses, making it more challenging.
Real-Time Updates: The game window updates in real-time, displaying the current falling shape and locked pieces.
Collision Detection: Ensures that pieces stop falling when they reach the bottom or hit other pieces.
Game Over Condition: The game detects when no more available spaces are left, signaling the end of the game.
What You’ll Learn:
Multi-dimensional list processing for the game grid.
How to use Pygame to create interactive game windows and manage graphics.
Basic game loops, real-time updates, and event handling.
Collision detection and grid-based game mechanics.
A structured approach to managing falling pieces, rotations, and locked positions.
How to Run:
Clone this repository.
Ensure you have Python 3.x and the Pygame library installed.
Run the main.py file to start the game.
bash
Copy code
git clone <your-repo-url>
cd <your-repo-directory>
python main.py
Future Improvements:
Adding scoring and high score saving functionality.
Implementing a start menu and end screen.
Advanced difficulty levels and speed increments.
