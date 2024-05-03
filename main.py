fun bubbleSort(numbers: MutableList<Int>) {
    val n = numbers.size
    for (i in 0 until n - 1) {
        for (j in 0 until n - i - 1) {
            if (numbers[j] > numbers[j + 1]) {
                // Обмен значениями
                val temp = numbers[j]
                numbers[j] = numbers[j + 1]
                numbers[j + 1] = temp
            }
        }
    }
}

fun main() {
    println("Введите числа, разделенные пробелом:")
    val input = readLine()
    val numbers = input?.split(" ")?.map { it.toInt() }?.toMutableList()

    if (numbers != null) {
        bubbleSort(numbers)
        println("Отсортированный список: $numbers")
    } else {
        println("Ошибка: введен некорректный список чисел.")
    }
}
