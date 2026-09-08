-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 31-10-2024 a las 19:24:21
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_clc1`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria`
--

CREATE TABLE `categoria` (
  `cod_c` int(5) NOT NULL,
  `nom_c` tinytext DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categoria`
--

INSERT INTO `categoria` (`cod_c`, `nom_c`) VALUES
(2, 'trajes de baño'),
(3, 'vestidos'),
(4, 'bottoms'),
(5, 'abrigos y chaquetas'),
(6, 'amigurumis'),
(7, 'accesorios'),
(8, 'conjuntos'),
(9, 'personalizados'),
(10, 'otros productos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cliente`
--

CREATE TABLE `cliente` (
  `cod_cli` int(5) NOT NULL,
  `nom_cli` tinytext DEFAULT NULL,
  `corr_cli` varchar(70) DEFAULT NULL,
  `sexo_cli` tinytext DEFAULT NULL,
  `direc_cli` varchar(70) DEFAULT NULL,
  `tipoid_cli` tinytext DEFAULT NULL,
  `id_cli` bigint(20) DEFAULT NULL,
  `fn_cli` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cliente`
--

INSERT INTO `cliente` (`cod_cli`, `nom_cli`, `corr_cli`, `sexo_cli`, `direc_cli`, `tipoid_cli`, `id_cli`, `fn_cli`) VALUES
(0, 'camilo', 'rosu22@gmail.com', 'masculino', 'llanitos', 'ti', 1095179032, '0000-00-00'),
(1, 'mirian sanche', 'misa@gmail.com', 'femenino', 'calle 67#76-89 calarca quindio', 'cedula de ciudadania', 167890658, '1879-12-08'),
(2, 'jairo parra', 'japa@gmail.com', 'masculino', 'calle 46#75-89 armenia quindio', 'cedula de ciudadania', 1748979775, '1990-06-05'),
(3, 'lina giraldo', 'linag@gmail.com', 'femenino', 'calle 6#97-68 circasia quindio', 'cedula de ciudadania', 1487575993, '2000-12-12'),
(4, 'alberto toro', 'albtoro@gmail.com', 'masculino', 'calle 23#5-7 salento quindio', 'tarjeta de identidad', 39286488, '2008-03-02'),
(5, 'cesar ballen', 'cesarb@gmail.com', 'masculino', 'calle 7#76-97 calarca quindio', 'cedula de ciudadania', 98264629, '1999-01-23'),
(6, 'samuel lopez', 'samulopez@gmail.com', 'masculino', 'calle 6#65-68 filandia quindio', 'tarjeta de identidad', 61736876, '2007-08-02'),
(7, 'maria osorio', 'mariao@gmail.com', 'femenino', 'calle 7#86-89 calarca quindio', 'cedula de ciudadania', 585856548, '2001-04-12'),
(8, 'karol arguello', 'karola@gmail.com', 'femenino', 'calle 1#64-87 filandia quindio', 'tarjeta de identidad', 72637678, '2007-04-12'),
(9, 'francisco medina', 'medinafr@gmail.com', 'masculino', 'calle 67#64-67 calarca quindio', 'cedula de ciudadania', 739864947, '1989-11-24'),
(10, 'maribel prieto', 'marip@gmail.com', 'femenino', 'calle 25#54-87 circasia quindio', 'cedula de ciudadania', 82768746, '1985-01-21'),
(90, 'juan', 'cam', 'masculino', 'valcones', 'cedula', 1095179032, '1980-01-02');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedido`
--

CREATE TABLE `pedido` (
  `cod_pe` int(5) NOT NULL,
  `f_pe` date DEFAULT NULL,
  `cant_pe` int(10) DEFAULT NULL,
  `vt_pe` varchar(10) DEFAULT NULL,
  `cod_cli1` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pedido`
--

INSERT INTO `pedido` (`cod_pe`, `f_pe`, `cant_pe`, `vt_pe`, `cod_cli1`) VALUES
(2, '2002-02-02', 20, '$130.000', 2),
(3, '2003-03-03', 6, '$200.000', 3),
(4, '2004-04-04', 1, '$20.000', 4),
(5, '2005-05-05', 2, '$80.000', 5),
(6, '2006-06-06', 5, '$400.000', 6),
(90, '2024-10-23', 2, '$130.002', 90);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `producto`
--

CREATE TABLE `producto` (
  `cod_p` int(5) NOT NULL,
  `col_p` tinytext DEFAULT NULL,
  `tam_p` tinytext DEFAULT NULL,
  `tipo_p` tinytext DEFAULT NULL,
  `pre_p` varchar(10) DEFAULT NULL,
  `desc_p` varchar(10) DEFAULT NULL,
  `nom_p` tinytext DEFAULT NULL,
  `cod_prov1` int(5) DEFAULT NULL,
  `cod_c1` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `producto`
--

INSERT INTO `producto` (`cod_p`, `col_p`, `tam_p`, `tipo_p`, `pre_p`, `desc_p`, `nom_p`, `cod_prov1`, `cod_c1`) VALUES
(2, 'rojo', 's', 'trajes de baño', '$100.002', '10%', 'agua', 2, 2),
(3, 'rosado', 'm', 'vestidos', '$90.000', '5%', 'jardin', 3, 3),
(4, 'verde', '7', 'bottoms', '$70.000', '0%', 'campana', 4, 4),
(5, 'blanco', 'xl', 'abrigos y chaquetas', '$120.000', '10%', 'rosas', 5, 5),
(6, 'azul', '45cm', 'amigurumis', '$50.000', '10%', 'flor', 6, 6),
(7, 'negro', 'xs', 'accesorios', '$20.000', '0%', 'rot', 7, 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedor`
--

CREATE TABLE `proveedor` (
  `cod_prov` int(5) NOT NULL,
  `nom_prov` tinytext DEFAULT NULL,
  `tel_prov` varchar(20) DEFAULT NULL,
  `trans_prov` varchar(7) DEFAULT NULL,
  `edad_prov` bigint(3) DEFAULT NULL,
  `direc_prov` varchar(70) DEFAULT NULL,
  `sexo_prov` tinytext DEFAULT NULL,
  `tipoid_prov` tinytext DEFAULT NULL,
  `id_prov` bigint(20) DEFAULT NULL,
  `corr_prov` varchar(70) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proveedor`
--

INSERT INTO `proveedor` (`cod_prov`, `nom_prov`, `tel_prov`, `trans_prov`, `edad_prov`, `direc_prov`, `sexo_prov`, `tipoid_prov`, `id_prov`, `corr_prov`) VALUES
(1, 'salome diaz', '3125467890', 'utr456', 46, 'calle 45#56-75', 'femenino', 'cedula de ciudadania', 454654546, 'salod@gmail.com'),
(2, 'silvana agudelo', '3114236789', 'jst048', 26, 'calle 45#12-11', 'femenino', 'cedula de ciudadania', 253636545, 'silvia@gmail.com'),
(3, 'emanuel delgado', '3167809787', 'gug496', 69, 'calle 3#4-5', 'masculino', 'cedula de ciudadania', 33678927, 'delgadoe@gmail.com'),
(4, 'isabella arenas', '3008907634', 'vgt257', 57, 'calle 34#12-45', 'femenino', 'cedula de ciudadania', 134675675, 'isaare@gmail.com'),
(5, 'geronimo estrada', '3207834567', 'ijo409', 37, 'calle 56#12-89', 'masculino', 'cedula de ciudadania', 345787557, 'geroes@gmail.com'),
(6, 'mariana bermudez', '3109546723', 'lao401', 29, 'calle 56#12-98', 'femenino', 'cedula de ciudadania', 146865784, 'marib@gmail.com'),
(7, 'matias quintero', '3216723456', 'qut139', 35, 'calle 7#56-98', 'masculino', 'cedula de ciudadania', 139686837, 'matiq@gmail.com'),
(8, 'sahory luna', '315670309', 'gtf500', 28, 'calle 57#97-23', 'femenino', 'cedula de ciudadania', 170472656, 'lunas@gmail.com'),
(9, 'julian loaiza', '3187659809', 'aaa000', 35, 'calle 5#9-9', 'masculino', 'cedula de ciudadania', 1468548958, 'julianl@gmail.com'),
(10, 'leidy marin', '3116578909', 'uty376', 29, 'calle 9#1-2', 'femenino', 'cedula de ciudadania', 9785357, 'leidym@gmail.com'),
(90, 'salome dfvjf', '3205843695', 'moto', 20, 'circasia', 'masculino', 'cedula', 33333333, 'prov@gmail.com');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE `usuario` (
  `cod_us` int(5) NOT NULL,
  `nom_us` tinytext DEFAULT NULL,
  `con_us` varchar(20) DEFAULT NULL,
  `correo_usu` text NOT NULL,
  `rol` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`cod_us`, `nom_us`, `con_us`, `correo_usu`, `rol`) VALUES
(1, 'YOmbibgnb', 'camivfvfvdfv@gmail.c', 'vdfvfvfdvdf', 'admin'),
(2, 'luisa giraldo', 'fhgbf5785', '', NULL),
(3, 'camilo meneses', 'sjmg3686', '', NULL),
(5, 'laura ariza', 'hbcuih389748', '', NULL),
(6, 'sofia petevi', 'hdvh639486', '', NULL),
(7, 'samuel lopez', 'nkdnv673246', '', NULL),
(8, 'francisco medina', 'hdjhv6t348', '', NULL),
(9, 'miriam sanchez', 'hcjdb73647', '', NULL),
(10, 'jose puentes', 'biuvfh783ybf', '', NULL),
(11, 'marible prieto', 'hjbciu7y4hf', '', NULL),
(12, 'YOmbibgnb', ' mgm gibfgnjgngbi', 'camilo88@gmail.com', 'admin'),
(13, 'luisa ', 'camilo@gmail.com', 'dccd', NULL),
(14, 'adminfjfj', 'camimeneses@gmail.co', '123456', NULL),
(15, 'joder', 'camimeneses21@gmail.', '123456789', NULL),
(16, 'joder', 'camimeneses21@gmail.', '123456789', NULL),
(17, 'camilooistetioufuv', 'camimeneses21@gmail.', '123456789', NULL),
(18, 'cami', 'camimeneses88@gmail.', '123456789', NULL),
(19, 'cggcg', 'camimeneses66@gmail.', '123456y', NULL),
(20, 'luisa', 'camivfvfvdfv@gmail.c', '1234567', NULL),
(21, 'MMFMFM', 'camil@gmail.com', 'camilo', NULL),
(22, 'luisa111', 'luisa111@gmail.com', 'luisa', NULL),
(23, 'fefu4jf', 'camilll', 'camimeneses123@gmail.com', NULL),
(24, 'ariza', 'ariza123', 'ariza@gmail.com', NULL),
(25, 'yo', 'yo12345', 'yo@gmail.com', NULL),
(26, 'nooooo', 'nooooo', 'luisa@gmail.com', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas`
--

CREATE TABLE `ventas` (
  `cod_ven` int(5) NOT NULL,
  `cod_pe1` int(5) DEFAULT NULL,
  `cod_p1` int(5) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `ventas`
--

INSERT INTO `ventas` (`cod_ven`, `cod_pe1`, `cod_p1`) VALUES
(4, 4, 5),
(5, 6, 6);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `categoria`
--
ALTER TABLE `categoria`
  ADD PRIMARY KEY (`cod_c`);

--
-- Indices de la tabla `cliente`
--
ALTER TABLE `cliente`
  ADD PRIMARY KEY (`cod_cli`);

--
-- Indices de la tabla `pedido`
--
ALTER TABLE `pedido`
  ADD PRIMARY KEY (`cod_pe`),
  ADD KEY `cod_cli1` (`cod_cli1`);

--
-- Indices de la tabla `producto`
--
ALTER TABLE `producto`
  ADD PRIMARY KEY (`cod_p`),
  ADD KEY `cod_prov1` (`cod_prov1`),
  ADD KEY `cod_c1` (`cod_c1`);

--
-- Indices de la tabla `proveedor`
--
ALTER TABLE `proveedor`
  ADD PRIMARY KEY (`cod_prov`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`cod_us`);

--
-- Indices de la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD PRIMARY KEY (`cod_ven`),
  ADD KEY `id_pe1` (`cod_pe1`),
  ADD KEY `id_pro1` (`cod_p1`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `cod_us` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT de la tabla `ventas`
--
ALTER TABLE `ventas`
  MODIFY `cod_ven` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `pedido`
--
ALTER TABLE `pedido`
  ADD CONSTRAINT `pedido_ibfk_1` FOREIGN KEY (`cod_cli1`) REFERENCES `cliente` (`cod_cli`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `producto`
--
ALTER TABLE `producto`
  ADD CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`cod_prov1`) REFERENCES `proveedor` (`cod_prov`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `producto_ibfk_2` FOREIGN KEY (`cod_c1`) REFERENCES `categoria` (`cod_c`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `ventas`
--
ALTER TABLE `ventas`
  ADD CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`cod_p1`) REFERENCES `producto` (`cod_p`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `ventas_ibfk_2` FOREIGN KEY (`cod_pe1`) REFERENCES `pedido` (`cod_pe`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
