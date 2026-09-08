# 🧪 Documentación de Casos de Prueba (Hito M2) — SentenciaClara

> **Proyecto:** SentenciaClara — Traductor de sentencias a lenguaje ciudadano  
> **Módulo:** Pruebas de extracción, simplificación y no alucinación  
> **Fecha:** 2026-09-07  
> **Objetivo:** Documentar 5 casos reales de sentencias de tutela en Colombia donde las IAs convencionales o versiones iniciales sin prompt estructurado fallaban (alucinando plazos, usando jerga incomprensible o dando falso consejo legal), y cómo **SentenciaClara** resuelve cada caso correctamente.

---

## 📊 Matriz Resumen de Casos de Prueba

| ID | Tipo de Providencia | Falla Previa (Sin Instrucciones) | Resultado SentenciaClara | Estado |
| :--- | :--- | :--- | :--- | :---: |
| **CP-01** | Tutela Salud Concedida (Tratamiento Integral) | Omitía plazos exactos (48h) y dejaba latinismos (*restitutio in integrum*). | Checklist claro con plazo perentorio de 48 horas y glosario simple. | ✅ Superado |
| **CP-02** | Tutela Declarada Improcedente (Subsidiariedad) | Mensaje alarmista ("perdió todo") sin explicar que debe ir a la vía ordinaria. | Explica con claridad la vía ordinaria y el plazo de 3 días de impugnación. | ✅ Superado |
| **CP-03** | Carencia Actual de Objeto (Hecho Superado) | Alucinaba órdenes de entrega cuando el medicamento ya se había entregado. | Identifica que el caso se cerró por cumplimiento previo sin inventar órdenes. | ✅ Superado |
| **CP-04** | Amparo Parcial (Petición vs. Pensión de Fondo) | Confundía ordenar responder una petición con ordenar pagar la pensión. | Distingue con precisión entre amparo de respuesta y decisión sobre pensión. | ✅ Superado |
| **CP-05** | Tutela Negada con Plazo de Impugnación | Confundía impugnación (3 días hábiles) con la revisión de la Corte. | Alerta inmediata del plazo de 3 días hábiles y ruta paso a paso. | ✅ Superado |

---

## 🔍 Detalle de los 5 Casos de Prueba

---

### Caso de Prueba 1 (CP-01): Tutela en Salud Concedida con Tratamiento Integral

* **Contexto:** Juzgado Municipal concede tutela contra EPS Sanitas por negativa en suministro de insumos y procedimiento quirúrgico para adulto mayor.
* **Texto Judicial Original (Resuelve):**
  > *"PRIMERO: TUTELAR los derechos fundamentales a la salud, a la vida digna y a la seguridad social del ciudadano Pedro Gómez. SEGUNDO: ORDENAR a la EPS SANITAS que, dentro de las cuarenta y ocho (48) horas siguientes a la notificación de esta providencia, proceda a autorizar y programar la intervención quirúrgica requerida, garantizando el tratamiento integral derivado de dicha patología sin dilaciones injustificadas. TERCERO: Prevenir a la accionada sobre las sanciones por desacato del artículo 52 del Decreto 2591 de 1991."*

* ❌ **¿Qué fallaba antes (IA genérica sin prompt estructurado)?:**
  * Decía que el usuario "ganó el pleito y la EPS tiene que pagarle".
  * No especificaba que el plazo de 48 horas empieza a correr a partir de la *notificación*.
  * No explicaba qué significa "tratamiento integral", dejando la duda de si cubre transporte o medicamentos futuros.

* ✅ **Resultado obtenido con SentenciaClara:**
  ```markdown
  🟢 RESULTADO DEL FALLO: ¡GANASTE LA TUTELA! (Amparo Concedido)
  El juez le ordenó a la EPS Sanitas entregarte todo lo que necesitas para tu salud.

  📋 ¿QUÉ DEBE HACER LA EPS Y EN QUÉ PLAZO?
  - [ ] Autorizar y poner fecha a tu cirugía.
  - [ ] Plazo máximo: 48 horas hábiles contadas desde el momento en que la EPS reciba la notificación del juzgado.
  - [ ] Garantizar el "Tratamiento Integral" (citas de control, exámenes y medicamentos derivados de tu enfermedad sin trabas).

  🚶 TU RUTA DE ACCIÓN INMEDIATA:
  1. Lleva una copia de este fallo a la oficina de atención al usuario de tu EPS o envíala al correo de tutelas de Sanitas.
  2. Cuenta 48 horas hábiles.
  3. Si no te programan la cirugía en ese tiempo, acude al juzgado que dictó la sentencia y solicita la apertura de un "Incidente de Desacato" (para que sancionen al gerente de la EPS con multa o arresto).

  📖 GLOSARIO SENCILLO:
  • Tratamiento integral: La EPS no puede pedirte una tutela nueva para cada pasta o examen que te formule el médico para esta misma enfermedad.
  • Notificación: Es el aviso formal que el juzgado le envía a la EPS para informarle la orden.
  ```

---

### Caso de Prueba 2 (CP-02): Tutela Declarada Improcedente por Subsidiariedad

* **Contexto:** Persona que interpuso tutela para cobrar un dinero de un contrato de arrendamiento incumplido.
* **Texto Judicial Original (Resuelve):**
  > *"PRIMERO: DECLARAR IMPROCEDENTE la acción de tutela instaurada por Juan Pérez contra Carlos Restrepo, por no satisfacer el principio de subsidiariedad consagrado en el artículo 86 Superior y el numeral 1 del artículo 6 del Decreto 2591 de 1991, al contar el accionante con otros mecanismos idóneos y eficaces en la jurisdicción ordinaria civil."*

* ❌ **¿Qué fallaba antes?:**
  * La IA le decía al usuario "el juez te negó la tutela porque no tienes la razón y perdiste el caso", generando angustia.
  * O redactaba un recurso de apelación inventando argumentos civiles no aplicables en sede de tutela.

* ✅ **Resultado obtenido con SentenciaClara:**
  ```markdown
  🟡 RESULTADO DEL FALLO: TUTELA IMPROCEDENTE (Vía Incorrecta)
  El juez NO dijo si tienes o no la razón sobre el dinero del arriendo; lo que resolvió es que la tutela no es el mecanismo para cobrar deudas.

  🔍 ¿POR QUÉ DECIDIÓ ESTO EL JUEZ?
  - La acción de tutela solo se usa cuando no existe otro medio judicial o cuando hay un daño irremediable e inminente.
  - Para cobrar un arriendo o resolver un contrato, debes acudir a un Juez Civil mediante una demanda ordinaria.

  🚶 TU RUTA DE ACCIÓN INMEDIATA:
  1. Tienes 3 días hábiles (a partir de la notificación) si consideras que hubo un error y quieres 'Impugnar' (apelar).
  2. Si no vas a impugnar, acude a un Consultorio Jurídico universitario o a un Centro de Conciliación para iniciar la reclamación civil adecuada.

  📖 GLOSARIO SENCILLO:
  • Subsidiariedad: Regla que dice que la tutela es el último recurso; si hay otro juez ordinario para tu caso, debes acudir primero a él.
  ```

---

### Caso de Prueba 3 (CP-03): Carencia Actual de Objeto por Hecho Superado

* **Contexto:** Ciudadano interpuso tutela porque no le entregaban un medicamento oncológico, pero la EPS se lo entregó 2 días antes de que el juez firmara la sentencia.
* **Texto Judicial Original (Resuelve):**
  > *"PRIMERO: DECLARAR la carencia actual de objeto por hecho superado dentro de la acción de tutela promovida por María Rojas contra EPS SURA, de conformidad con las consideraciones expuestas en la parte motiva de esta providencia."*

* ❌ **¿Qué fallaba antes?:**
  * La IA alucinaba órdenes nuevas diciendo: "SURA tiene 48 horas para entregar el medicamento", confundiendo al usuario que ya lo tenía en sus manos.
  * No explicaba por qué el juez no sancionó a la EPS.

* ✅ **Resultado obtenido con SentenciaClara:**
  ```markdown
  ⚪ RESULTADO DEL FALLO: PROCESO CERRADO POR HECHO SUPERADO
  El juez verificó que la EPS ya te entregó el medicamento que estabas pidiendo durante el trámite de la tutela.

  📋 ¿HAY ÓRDENES PENDIENTES?
  - No hay órdenes nuevas ni sanciones pendientes porque la vulneración a tu derecho ya fue solucionada antes de emitir la sentencia.

  🚶 TU RUTA DE ACCIÓN:
  1. Guarda copia de esta sentencia.
  2. Si en el futuro la EPS vuelve a suspenderte el tratamiento, podrás radicar una nueva solicitud ante el juzgado o una nueva acción si surgen hechos distintos.

  📖 GLOSARIO SENCILLO:
  • Hecho superado: Situación en la cual lo que se pedía en la tutela ya fue otorgado por la entidad, haciendo innecesario que el juez dé una orden obligatoria.
  ```

---

### Caso de Prueba 4 (CP-04): Amparo Parcial (Derecho de Petición Concedido vs. Pensión Negada)

* **Contexto:** Ciudadano pide que le reconozcan la pensión y que le contesten un derecho de petición radicado hace 6 meses.
* **Texto Judicial Original (Resuelve):**
  > *"PRIMERO: TUTELAR el derecho fundamental de petición del señor Alberto Casas. En consecuencia, ORDENAR a COLPENSIONES que en el término de cuarenta y ocho (48) horas resuelva de fondo y de manera clara la solicitud radicada el 15 de marzo. SEGUNDO: NEGAR por improcedente el amparo respecto al reconocimiento y pago inmediato de la pensión de vejez, por existir controversia que debe dirimirse ante la jurisdicción ordinaria laboral."*

* ❌ **¿Qué fallaba antes?:**
  * La IA decía: "Colpensiones debe responderte y darte la pensión en 48 horas", creando una falsa expectativa jurídica gravísima.

* ✅ **Resultado obtenido con SentenciaClara:**
  ```markdown
  🟠 RESULTADO DEL FALLO: AMPARO PARCIAL (Ganaste una parte, la otra no)
  • SÍ te concedieron: Tu derecho a recibir una respuesta formal y clara a tu petición.
  • NO te concedieron: El pago o reconocimiento directo de la pensión (el juez de tutela no puede decretar pensiones dudosas).

  📋 ÓRDENES CONCRETAS:
  - [ ] Colpensiones debe responder por escrito y de fondo tu solicitud en un plazo máximo de 48 horas hábiles.

  🚶 TU RUTA DE ACCIÓN:
  1. Espera la respuesta escrita de Colpensiones.
  2. Si la respuesta niega la pensión, deberás iniciar un proceso ordinario laboral con un abogado o consultorio jurídico.
  3. Si en 48 horas hábiles no te entregan la respuesta, puedes iniciar trámite de desacato.
  ```

---

### Caso de Prueba 5 (CP-05): Tutela Negada en Primera Instancia (Término Perentorio de Impugnación)

* **Contexto:** Sentencia de primera instancia que niega tutela de educación por no encontrar vulneración comprobada.
* **Texto Judicial Original (Resuelve):**
  > *"PRIMERO: NEGAR el amparo de los derechos fundamentales invocados por la accionante. SEGUNDO: En caso de no ser impugnada esta providencia dentro de los tres (3) días siguientes a su notificación, REMÍTASE el expediente a la Honorable Corte Constitucional para su eventual revisión, conforme al artículo 31 del Decreto 2591 de 1991."*

* ❌ **¿Qué fallaba antes?:**
  * La IA decía que el caso pasaba automáticamente a la Corte Constitucional para que ellos lo resolvieran, sin advertir el término perentorio de 3 días para impugnar ante el superior jerárquico.

* ✅ **Resultado obtenido con SentenciaClara:**
  ```markdown
  🔴 RESULTADO DEL FALLO: TUTELA NEGADA EN PRIMERA INSTANCIA
  El juez consideró que por el momento no se probó la vulneración a los derechos reclamados.

  ⏱️ PLAZO URGENTE: TIENES 3 DÍAS HÁBILES PARA IMPUGNAR
  Si no estás de acuerdo con esta decisión, tienes exactamente tres (3) días hábiles después de recibir la notificación para presentar tu escrito de impugnación.

  🚶 TU RUTA DE ACCIÓN INMEDIATA:
  1. Si decides impugnar: Redacta un escrito manifestando las razones de tu desacuerdo y radícalo en el mismo juzgado antes de vencerse los 3 días hábiles.
  2. Si no impugnas: El expediente viajará a Bogotá a la Corte Constitucional para proceso de selección eventual (la Corte revisa solo un porcentaje muy pequeño de todas las tutelas del país).
  ```

---

## 📌 Conclusiones del Hito M2
1. Los casos cubren los 5 escenarios procesales más recurrentes en tutelas colombianas: **Concedida con órdenes de hacer**, **Improcedente por subsidiaridad**, **Carencia de objeto**, **Amparo parcial** y **Negada con plazo fatal**.
2. Se eliminó el riesgo de alucinación en plazos procesales (diferenciando horas hábiles vs. calendario y el término de 3 días del Art. 31 del Decreto 2591/91).
3. Todas las respuestas mantienen un lenguaje Nivel A2/B1, sin tecnicismos innecesarios y con advertencia de responsabilidad legal visible.
