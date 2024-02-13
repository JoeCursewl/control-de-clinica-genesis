-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-07-2023 a las 05:33:58
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `cl_database`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cl_historias`
--

CREATE TABLE `cl_historias` (
  `cl_id_hist` int(11) NOT NULL,
  `cl_cedula` int(11) NOT NULL,
  `cl_fecha` varchar(30) NOT NULL,
  `cl_peso` varchar(30) NOT NULL,
  `cl_tension` int(20) NOT NULL,
  `cl_talla` int(20) NOT NULL,
  `cl_exam_fisico` varchar(255) NOT NULL,
  `cl_sintomas` varchar(255) NOT NULL,
  `cl_diagnostico` varchar(255) NOT NULL,
  `cl_tratamiento` varchar(255) NOT NULL,
  `cl_antecedentes` varchar(255) NOT NULL,
  `cl_ante_family` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

--
-- Volcado de datos para la tabla `cl_historias`
--

INSERT INTO `cl_historias` (`cl_id_hist`, `cl_cedula`, `cl_fecha`, `cl_peso`, `cl_tension`, `cl_talla`, `cl_exam_fisico`, `cl_sintomas`, `cl_diagnostico`, `cl_tratamiento`, `cl_antecedentes`, `cl_ante_family`) VALUES
(13, 30853741, '25-07-2023', '52', 50, 28, 'Examen fisicio en esta parte', 'Sintomas en esta parte', 'Diagnostico en esta parte', 'tratamiento medico en esta parte', 'Antecedentes del paciente en esta parte', 'antecedentes en esta parte'),
(14, 30853741, '25-03-2023', '52', 14, 1251, 'dsadasdasdasdasdasdasdasd', 'asdasdasdasdasdasda', 'sadasdsadasdasdasd', 'asdasdasdasdsa', 'dasdasdasdasdasd', 'dasdasdasdasdasdasd'),
(15, 27416435, '25-07-2023', '50', 50, 23, 'Examen fisicio en esta parte', 'Síntomas en esta parte del programa ', 'Diagnóstico del programa en esta parte', 'Tratamiento médico en esta parte', 'Anteceddentes del paciente', 'Antecedentes familiares en esta parte'),
(16, 27416435, '28-07-2023', '50', 52, 28, 'Examen fisico en esta parte de nuevo xoxo', 'Sintomas en esta parte de nuevo de nuevo owo', 'diagnostico en esta parte de nuevo ', 'Tratmiento medico en esta parte de nuevo', 'Antecedentes del paciente de lo que se habia hecho', 'Antecedentes familiares en esta parte del sistema');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cl_pacientes`
--

CREATE TABLE `cl_pacientes` (
  `cl_cedula` int(11) NOT NULL,
  `cl_nombres` varchar(30) NOT NULL,
  `cl_apellidos` varchar(30) NOT NULL,
  `cl_dir` varchar(30) NOT NULL,
  `cl_fecha_nac` varchar(30) NOT NULL,
  `cl_genero` varchar(20) NOT NULL,
  `cl_telefono` varchar(20) NOT NULL,
  `cl_edad` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

--
-- Volcado de datos para la tabla `cl_pacientes`
--

INSERT INTO `cl_pacientes` (`cl_cedula`, `cl_nombres`, `cl_apellidos`, `cl_dir`, `cl_fecha_nac`, `cl_genero`, `cl_telefono`, `cl_edad`) VALUES
(27416435, 'Stella Rose', 'Bennett O\'Connell', 'Her house', '22-05-2000', 'Mujer', '04264544', 23),
(30853507, 'Anthony Cursewl', 'Bennett O\'Connel', 'Mi casa xoxo.', '11-04-2003', 'Hombre', '4261792396', 22),
(30853741, 'Diana Cursewl', 'Bennett', 'Mi casita', '11-04-2003', 'Mujer', '04261792396', 20);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cl_users`
--

CREATE TABLE `cl_users` (
  `id_user` int(11) NOT NULL,
  `cl_usuario` varchar(30) NOT NULL,
  `cl_password` varchar(35) NOT NULL,
  `cl_correo` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

--
-- Volcado de datos para la tabla `cl_users`
--

INSERT INTO `cl_users` (`id_user`, `cl_usuario`, `cl_password`, `cl_correo`) VALUES
(4, 'root_user', 'root_password1214', 'root@localhost.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cl_users_asistentes`
--

CREATE TABLE `cl_users_asistentes` (
  `id_user` int(11) NOT NULL,
  `cl_usuario` varchar(30) NOT NULL,
  `cl_password` varchar(30) NOT NULL,
  `cl_correo` varchar(35) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cl_users_medicos`
--

CREATE TABLE `cl_users_medicos` (
  `id_user` int(11) NOT NULL,
  `cl_usuario` varchar(30) NOT NULL,
  `cl_password` varchar(30) NOT NULL,
  `cl_correo` varchar(38) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf16 COLLATE=utf16_spanish_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `cl_historias`
--
ALTER TABLE `cl_historias`
  ADD PRIMARY KEY (`cl_id_hist`),
  ADD KEY `cl_cedula` (`cl_cedula`);

--
-- Indices de la tabla `cl_pacientes`
--
ALTER TABLE `cl_pacientes`
  ADD PRIMARY KEY (`cl_cedula`);

--
-- Indices de la tabla `cl_users`
--
ALTER TABLE `cl_users`
  ADD PRIMARY KEY (`id_user`);

--
-- Indices de la tabla `cl_users_asistentes`
--
ALTER TABLE `cl_users_asistentes`
  ADD PRIMARY KEY (`id_user`);

--
-- Indices de la tabla `cl_users_medicos`
--
ALTER TABLE `cl_users_medicos`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `cl_historias`
--
ALTER TABLE `cl_historias`
  MODIFY `cl_id_hist` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de la tabla `cl_users`
--
ALTER TABLE `cl_users`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `cl_users_asistentes`
--
ALTER TABLE `cl_users_asistentes`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `cl_users_medicos`
--
ALTER TABLE `cl_users_medicos`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `cl_historias`
--
ALTER TABLE `cl_historias`
  ADD CONSTRAINT `cl_historias_ibfk_1` FOREIGN KEY (`cl_cedula`) REFERENCES `cl_pacientes` (`cl_cedula`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
