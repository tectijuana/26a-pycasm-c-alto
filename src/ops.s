.global suma_array
.global contar_pares
.global dot_product

// suma de arreglo
suma_array:
    mov x2, #0      // i
    mov x3, #0      // suma

loop_suma:
    cmp x2, x1
    bge fin_suma

    ldr x4, [x0, x2, lsl #3]
    add x3, x3, x4

    add x2, x2, #1
    b loop_suma

fin_suma:
    mov x0, x3
    ret

// contar pares
contar_pares:
    mov x2, #0
    mov x3, #0

loop_pares:
    cmp x2, x1
    bge fin_pares

    ldr x4, [x0, x2, lsl #3]
    and x5, x4, #1
    cmp x5, #0
    bne no_par

    add x3, x3, #1

no_par:
    add x2, x2, #1
    b loop_pares

fin_pares:
    mov x0, x3
    ret

// producto punto
dot_product:
    mov x3, #0
    mov x4, #0

loop_dot:
    cmp x3, x2
    bge fin_dot

    ldr x5, [x0, x3, lsl #3]
    ldr x6, [x1, x3, lsl #3]

    mul x7, x5, x6
    add x4, x4, x7

    add x3, x3, #1
    b loop_dot

fin_dot:
    mov x0, x4
    ret
