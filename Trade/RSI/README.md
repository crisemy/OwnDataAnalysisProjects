# Analizador de Ethereum con Estrategia RSI

**Un script simple y visual para analizar Ethereum (ETH) usando el indicador RSI.**

Este notebook permite:
- Descargar los **precios históricos de Ethereum (ETH-USD)** desde 2025 hasta hoy
- Calcular el **RSI (Índice de Fuerza Relativa)** automáticamente con 14 períodos
- Identificar **momentos ideales de compra** (cuando ETH está "barato" - RSI < 30) 
- Detectar **momentos de venta** (cuando ETH está "caro" - RSI > 70)
- Ver un **gráfico claro** con el precio de ETH + flechas verdes (compra) y rojas (venta) + el RSI debajo
- **Simular cuánto ganarías** si hubieras seguido estas señales con $1000 USD inicial

## ¿Qué hace exactamente?

1. **Descarga datos reales** de ETH-USD (Yahoo Finance → CoinGecko como respaldo → Binance si falla todo)
2. **Calcula el RSI**: Mide si el precio sube/baja "demasiado rápido" 
   - **RSI < 30** = Sobreventa → **¡Posible compra!** (precio puede rebotar)
   - **RSI > 70** = Sobrecompra → **¡Posible venta!** (precio puede corregir)
3. **Genera señales automáticas** en el gráfico (triángulos verdes para comprar, rojos para vender)
4. **Simula la estrategia**: 
   - Empiezas con $1000 USD
   - **Compras TODO** tu ETH cuando aparece señal verde (y tienes cash)
   - **Vendes TODO** cuando aparece señal roja (y tienes ETH)
   - Al final te dice: *"Con $1000 inicial, terminarías con $X.XXX → +XXX% de ganancia"*

## Ejemplo

**Gráfico superior**: Línea azul del precio ETH + flechas de señales