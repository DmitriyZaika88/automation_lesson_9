# automation_lesson_9

Для запуска allure необходимо у кажжого теста написать конфинурацию --alluredir=allure-results, которая создает директорию allure-results после прохождения теста (далее, после повторного прохождения текстов, новые логи добавляются в папку)

Для создания отчета необходимо в powershell перейти в директорию с проектом (до папки allure-results) и ввести команду allure serve allure-results
 
![image](https://user-images.githubusercontent.com/54865508/231477448-b84ceb82-a2ae-44bb-ae71-1be54a127199.png)
