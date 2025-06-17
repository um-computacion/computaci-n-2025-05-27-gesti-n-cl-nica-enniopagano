Cómo ejecutar el sistema

El sistema se ejecuta con:
python CLI.py

El programa mostrará un menú interactivo donde podrás:
-Agregar pacientes y médicos
-Agendar turnos
-Emitir recetas
-Consultar historias clínicas
-Ver listados de datos

Cómo ejecutar las pruebas
Ejecutá las pruebas con el siguiente comando:

python -m unittest TestCLI.py
Esto ejecutará las pruebas automáticas que cubren los aspectos principales del sistema (verificación de duplicados, validaciones, agendamientos, recetas e historial clínico).

Explicación del diseño general
El sistema está estructurado en módulos separados por responsabilidad, facilitando el mantenimiento y la extensibilidad:

CLI.py: Interfaz de línea de comandos. Presenta el menú principal y conecta las opciones del usuario con la lógica de negocio.

clases:
-Clinica: Clase principal que coordina pacientes, médicos, turnos y recetas.
-Paciente, Medico, Especialidad, Turno, Receta, HistoriaClinica: Modelan cada entidad del sistema.
-excepciones: Contiene clases personalizadas para manejar errores específicos del dominio (por ejemplo, médico no disponible, receta inválida, etc.).

El sistema valida:
-Que no se ingresen pacientes o médicos duplicados.
-Que los turnos no se agenden en días no disponibles o si ya están ocupados.
-Que solo se emitan recetas si el paciente y médico existen y hay medicamentos.
Además, cada paciente tiene una historia clínica que guarda sus turnos y recetas emitidas.