# ---------- CHOICES---------------------
CHOICE_TIPO_ORGANISMO = [
    (None, ''),
    ('Admisión', 'Admisión'),
    ('Comisaria', 'Comisaria'),
    ('Institucional', 'Institucional'),
    ('Salud', 'Salud'),
    ('U.F.I.s', 'U.F.I.s'),
    ('Escuelas', 'Escuelas'),
    ('Zonal', 'Zonal'),
    ('Oficios judiciales', 'Oficios judiciales'),
    ('Politicas de genero', 'Politicas de genero'),
    ('Expediente civil', 'Expediente civil'),
]

CHOICE_JURISDICCION = [
    (None, ''),
    ('Nacional', 'Nacional'),
    ('Provincial', 'Provincial'),
    ('Municipal', 'Municipal'),
]

CHOICE_CIRCUITOS = [
    (None, ''),
    ('0397A', '0397A'),
    ('0397B', '0397B'),
    ('0397C', '0397C'),
    ('0397', '0397'),
    ('0400', '0400'),
    ('0401A', '0401A'),
    ('0401', '0401'),
    ('0402', '0402'),
]

CHOICE_LOCALIDAD = [
    (None, ''),
    ('San Miguel', 'San Miguel'),
    ('Bella Vista', 'Bella Vista'),
    ('Muñiz', 'Muñiz'),
    ('Santa María', 'Santa María'),
]

CHOICE_BARRIOS = [
    (None, ''),
    ('Altos de San José', 'Altos de San José'),
    ('Bello Horizonte', 'Bello Horizonte'),
    ('Colegio Máximo', 'Colegio Máximo'),
    ('Colibrí', 'Colibrí'),
    ('Constantini', 'Constantini'),
    ('Cuartel Segundo Cc.', 'Cuartel Segundo Cc.'),
    ('Don Alfonso', 'Don Alfonso'),
    ('La Gloria', 'La Gloria'),
    ('La Estrella', 'La Estrella'),
    ('La Guarida', 'La Guarida'),
    ('La Manuelita', 'La Manuelita'),
    ('Lomas de Mariló', 'Lomas de Mariló'),
    ('Los Paraísos', 'Los Paraísos'),
    ('Los Plátanos', 'Los Plátanos'),
    ('Macabi', 'Macabi'),
    ('María Rosa Mística', 'María Rosa Mística'),
    ('Mitre', 'Mitre'),
    ('Parque San Miguel', 'Parque San Miguel'),
    ('Parque San Ignacio', 'Parque San Ignacio'),
    ('Santa Brígida', 'Santa Brígida'),
    ('Sarmiento', 'Sarmiento'),
    ('Trujui', 'Trujui'),
    ('Santa María', 'Santa María'),
    ('San Antonio', 'San Antonio'),
    ('San Ignacio', 'San Ignacio'),
]

CHOICE_IMPACTO=[
    (None, ''),
    ('BAJO', 'BAJO'),
    ('MEDIO', 'MEDIO'),
    ('ALTO', 'ALTO'),
]
CHOICE_DIMENSIONES=[
    (None, ''),
    ('Familia', 'Familia'),
    ('Vivienda', 'Vivienda'),
    ('Salud', 'Salud'),
    ('Economía', 'Economía'),
    ('Educación', 'Educación'),
    ('Trabajo', 'Trabajo'),
]
CHOICE_TIPO_DE_DATOS=[
    (None, ''),
    ('Texto', 'Texto'),
    ('Fecha', 'Fecha'),
    ('Número', 'Número'),
    ('Booleano', 'Si/No'),
]
CHOICE_TIPO_DE_FORMULARIO=[
    (None, ''),
    ('Derivación', 'Derivación'),
    ('Admisión', 'Admisión'),
    ('Intervención', 'Intervención'),
    ('Otro', 'Otro'),
]

CHOICE_1A5=[
    (None, ''),
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('Más de 5', 'Más de 5'),
]

CHOICE_EMB_RIESGO=[
    (None, ''),
    ('Normal', 'Normal'),
    ('Adolescente', 'Adolescente'),
    ('De riesgo (Diabetes, Hipertension, Sífilis, etc.)', 'De riesgo (Diabetes, Hipertension, Sífilis, etc.)'),
]

CHOICE_EDUCACION=[
    (None, ''),
    ('Primario', 'Primario'),
    ('Secundario', 'Secundario'),
    ('Terciario', 'Terciario'),
    ('Universitario', 'Universitario'),
]
CHOICE_ESTADO=[
    (None, ''),
    ('Completo', 'Completo'),
    ('Incompleto', 'Incompleto'),
    ('En curso', 'En curso'),
    ('No aplica', 'No aplica'),
]
CHOICE_PLANES_SOCIALES=[
    (None, ''),
    ('AUH (Asignacion Universal por Hijo)', 'AUH (Asignacion Universal por Hijo)'),
    ('Asignación Universal por Embarazo', 'Asignación Universal por Embarazo'),
    ('Tarjeta Alimentar', 'Tarjeta Alimentar'),
    ('Potenciar Trabajo', 'Potenciar Trabajo'),
    ('Plan Más Vida', 'Plan Más Vida'),
    ('Plan 1000 Días (ANSES)', 'Plan 1000 Días (ANSES)'),
    ('Progresar', 'Progresar'),
    ('Cooperativas', 'Cooperativas'),
    ('Pensión por discapacidad', 'Pensión por discapacidad'),
    ('Pensión madre de 7 hijos', 'Pensión madre de 7 hijos'),
    ('Pensión por viudez', 'Pensión por viudez'),
]

CHOICE_CONTRATACION=[
    (None, ''),
    ('Relación de dependencia', 'Relación de dependencia'),
    ('Monotributista / Contratado', 'Monotributista / Contratado'),
    ('Informal con cobro mensual', 'Informal con cobro mensual'),
    ('Jornal', 'Jornal'),
    ('Changarín', 'Changarín'),
    ('Otro', 'Otro'),
]

CHOICE_SALA_POSTULA=[
    (None, ''),
    ('Bebés', 'Bebés'),
    ('Sala de 2', 'Sala de 2'),
    ('Sala de 3', 'Sala de 3'),
]
CHOICE_TURNO_POSTULA=[
    (None, ''),
    ('Mañana', 'Mañana'),
    ('Tarde', 'Tarde'),
]
CHOICE_TIPO_INGRESO=[
    (None, ''),
    ('Criteros autónomos de ingreso', 'Criteros autónomos de ingreso'),
    ('Motivo de falta de control o control insuficiente', 'Motivo de falta de control o control insuficiente'),
    ('Criterios combinables de ingreso', 'Criterios combinables de ingreso'),
    ('Criterios sociales para el ingreso', 'Criterios sociales para el ingreso'),
]
CHOICE_TIPO_IVI=[
    (None, ''),
    ('Madre o Cuidador principal', 'Madre o Cuidador principal'),
    ('Bebé, niño o niña', 'Bebé, niño o niña'),
    ('Familia', 'Familia'),
    ('Ajustes', 'Ajustes'),
]
CHOICE_NOSI=[
    (None, ''),
    ('SI', 'SI'),
    ('NO', 'NO'),
]
CHOICE_RESPONSABLES=[
    ('Garcia Maria Begoña','Garcia Maria Begoña'),
    ('Vivas Antonella','Vivas Antonella'),
    ('Rodriguez Vanina Natalia','Rodriguez Vanina Natalia'),
    ('Torres Liliana Yanet','Torres Liliana Yanet'),
    ('Palavecino Marianela Celeste','Palavecino Marianela Celeste'),
    ('Mancuso Agostina Lourdes','Mancuso Agostina Lourdes'),
    ('Autelli Florencia Belen','Autelli Florencia Belen'),
    ('Cardozo Claudia Yamila Noemi','Cardozo Claudia Yamila Noemi'),
    ('Ganduglia Lourdes Rocío','Ganduglia Lourdes Rocío'),
    ('Diaz Karen Marlene Sara','Diaz Karen Marlene Sara'),
    ('Bastrate Brenda Yamila','Bastrate Brenda Yamila'),
    ('Gonzalez Ana Laura','Gonzalez Ana Laura'),
    ('Azcurra Maria Luz','Azcurra Maria Luz'),
    ('Araoz Luisa Emilia','Araoz Luisa Emilia'),
]

CHOICE_ACCION_DESARROLLADA=[
    ('Se realizan entrevistas de acompañamiento/ seguimiento','Se realizan entrevistas de acompañamiento/ seguimiento'),
    ('Se la acompaño a realizar el tramite','Se la acompaño a realizar el tramite'),
    ('Se articulo con SL','Se articulo con SL'),
    ('Se articulo con 1000 dias','Se articulo con 1000 dias'),
    ('Se articulo con PDV','Se articulo con PDV'),
    ('Se articulo con asistencia critica/ Desarrollo social','Se articulo con asistencia critica/ Desarrollo social'),
    ('Se articulo con Salud por un turno','Se articulo con Salud por un turno'),
    ('Se articula con salud','Se articula con salud'),
    ('Se articulo con Salud Mental','Se articulo con Salud Mental'),
    ('Se artiulo con Servicio Local','Se artiulo con Servicio Local'),
    ('Se articulo con Politicas de genero','Se articulo con Politicas de genero'),
    ('Se realizo denuncia por violencia','Se realizo denuncia por violencia'),
    ('Se oriento para realizar la denuncia','Se oriento para realizar la denuncia'),
    ('Se articulo con educación/ FINES','Se articulo con educación/ FINES'),
    ('Se articulo con Potenciar trabajo','Se articulo con Potenciar trabajo'),
    ('Se brindo información','Se brindo información'),
    ('Se realizo un control del niño sano','Se realizo un control del niño sano'),
    ('Se articulo con una institución no municipal','Se articulo con una institución no municipal'),
]

CHOICE_1to40=[(i, str(i)) for i in range(1, 41)]

CHOICE_4to40=[(i, str(i)) for i in range(4, 41)]

CHOICE_VULNERACION=[
    (None, ''),
    ('ASI', 'ASI'),
    ('Violencia/negligencia', 'Violencia/negligencia'),
    ('Maltrato infantil', 'Maltrato infantil'),
    ('Incump. D. D. Asistencia', 'Incump. D. D. Asistencia'),
    ('Situación de calle', 'Situación de calle'),
    ('Riesgo habitacional/salud/alimenticio', 'Riesgo habitacional/salud/alimenticio'),
    ('Fuga de hogar', 'Fuga de hogar'),
    ('Adolescente en riesgo (embarazo/aborto)', 'Adolescente en riesgo (embarazo/aborto)'),
    ('Riesgo escolar', 'Riesgo escolar'),
    ('Conflictos con la ley', 'Conflictos con la ley'),
    ('Adicciones', 'Adicciones'),
    ('Niño en riesgo', 'Niño en riesgo'),
    ('Filiación y guardia', 'Filiación y guardia'),
    ('Otros', 'Otros'),
]