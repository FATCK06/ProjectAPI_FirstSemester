-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 24-Set-2025 às 13:22
-- Versão do servidor: 10.4.32-MariaDB
-- versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `sjc_dados_populacao`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `densidade_demografica_sjc_2010`
--

CREATE TABLE `densidade_demografica_sjc_2010` (
  `id` int(11) NOT NULL,
  `Municipio` varchar(255) DEFAULT NULL,
  `Populacao Total` int(11) DEFAULT NULL,
  `Populacao Urbana` int(11) DEFAULT NULL,
  `Populacao Urbana na Sede Municipal` int(11) DEFAULT NULL,
  `Populacao Total (%)` decimal(5,2) DEFAULT NULL,
  `Populacao Urbana (%)` decimal(5,2) DEFAULT NULL,
  `Populacao Urbana na Sede Municipal (%)` decimal(5,2) DEFAULT NULL,
  `Area Total (Km2)` decimal(10,2) DEFAULT NULL,
  `Densidade Demografica (Hab/Km2)` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `faixa_etaria_homens_2010`
--

CREATE TABLE `faixa_etaria_homens_2010` (
  `id` int(11) NOT NULL,
  `Indicador` varchar(255) DEFAULT NULL,
  `Ano` int(11) DEFAULT NULL,
  `Valor` int(11) DEFAULT NULL,
  `Unidade` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `faixa_etaria_mulheres_2010`
--

CREATE TABLE `faixa_etaria_mulheres_2010` (
  `id` int(11) NOT NULL,
  `Indicador` varchar(255) DEFAULT NULL,
  `Ano` int(11) DEFAULT NULL,
  `Valor` int(11) DEFAULT NULL,
  `Unidade` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `idade_sexo_2022`
--

CREATE TABLE `idade_sexo_2022` (
  `id` int(11) NOT NULL,
  `Ano` int(11) DEFAULT NULL,
  `Total` int(11) DEFAULT NULL,
  `Tipo` varchar(50) DEFAULT NULL,
  `0 a 4 anos` int(11) DEFAULT NULL,
  `5 a 9 anos` int(11) DEFAULT NULL,
  `10 a 14 anos` int(11) DEFAULT NULL,
  `15 a 19 anos` int(11) DEFAULT NULL,
  `20 a 24 anos` int(11) DEFAULT NULL,
  `25 a 29 anos` int(11) DEFAULT NULL,
  `30 a 34 anos` int(11) DEFAULT NULL,
  `35 a 39 anos` int(11) DEFAULT NULL,
  `40 a 44 anos` int(11) DEFAULT NULL,
  `45 a 49 anos` int(11) DEFAULT NULL,
  `50 a 54 anos` int(11) DEFAULT NULL,
  `55 a 59 anos` int(11) DEFAULT NULL,
  `60 a 64 anos` int(11) DEFAULT NULL,
  `65 a 69 anos` int(11) DEFAULT NULL,
  `70 a 74 anos` int(11) DEFAULT NULL,
  `75 a 79 anos` int(11) DEFAULT NULL,
  `80 a 84 anos` int(11) DEFAULT NULL,
  `85 a 89 anos` int(11) DEFAULT NULL,
  `90 a 94 anos` int(11) DEFAULT NULL,
  `95 a 99 anos` int(11) DEFAULT NULL,
  `100 anos ou mais` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `populacao_residencia_2022`
--

CREATE TABLE `populacao_residencia_2022` (
  `id` int(11) NOT NULL,
  `Ano` int(11) DEFAULT NULL,
  `Populacao residente` int(11) DEFAULT NULL,
  `Area unidade territorial` decimal(10,3) DEFAULT NULL,
  `Densidade` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `populacao_residente_sjc_2010`
--

CREATE TABLE `populacao_residente_sjc_2010` (
  `id` int(11) NOT NULL,
  `Categoria` varchar(255) DEFAULT NULL,
  `Indicador` varchar(255) DEFAULT NULL,
  `Ano` int(11) DEFAULT NULL,
  `Valor` int(11) DEFAULT NULL,
  `Unidade` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `densidade_demografica_sjc_2010`
--
ALTER TABLE `densidade_demografica_sjc_2010`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `faixa_etaria_homens_2010`
--
ALTER TABLE `faixa_etaria_homens_2010`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `faixa_etaria_mulheres_2010`
--
ALTER TABLE `faixa_etaria_mulheres_2010`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `idade_sexo_2022`
--
ALTER TABLE `idade_sexo_2022`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `populacao_residencia_2022`
--
ALTER TABLE `populacao_residencia_2022`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `populacao_residente_sjc_2010`
--
ALTER TABLE `populacao_residente_sjc_2010`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `densidade_demografica_sjc_2010`
--
ALTER TABLE `densidade_demografica_sjc_2010`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `faixa_etaria_homens_2010`
--
ALTER TABLE `faixa_etaria_homens_2010`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `faixa_etaria_mulheres_2010`
--
ALTER TABLE `faixa_etaria_mulheres_2010`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `idade_sexo_2022`
--
ALTER TABLE `idade_sexo_2022`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `populacao_residencia_2022`
--
ALTER TABLE `populacao_residencia_2022`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `populacao_residente_sjc_2010`
--
ALTER TABLE `populacao_residente_sjc_2010`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
