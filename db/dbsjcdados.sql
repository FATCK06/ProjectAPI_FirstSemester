-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 25-Set-2025 às 16:55
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
-- Banco de dados: `dbsjcdados`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `dados_educacao`
--

CREATE TABLE `dados_educacao` (
  `id` int(11) NOT NULL,
  `ano` int(11) NOT NULL,
  `indicador` varchar(255) NOT NULL,
  `valor` int(11) NOT NULL,
  `descricao` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `densidade_demografica_sjc_2010`
--

CREATE TABLE `densidade_demografica_sjc_2010` (
  `id` int(11) NOT NULL,
  `Municipio` varchar(255) DEFAULT NULL,
  `Populacao_Total` int(11) DEFAULT NULL,
  `Populacao_Urbana` int(11) DEFAULT NULL,
  `Populacao_Urbana_na_Sede_Municipal` int(11) DEFAULT NULL,
  `Populacao_Total_` decimal(5,2) DEFAULT NULL,
  `Populacao_Urbana_` decimal(5,2) DEFAULT NULL,
  `Populacao_Urbana_na_Sede_Municipal_` decimal(5,2) DEFAULT NULL,
  `Area_Total_Km2` decimal(10,2) DEFAULT NULL,
  `Densidade_Demografica_Hab_Km2` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `docentes_por_dependencia_2010`
--

CREATE TABLE `docentes_por_dependencia_2010` (
  `id` int(11) NOT NULL,
  `Dependencia_Administrativa` varchar(255) DEFAULT NULL,
  `Docentes_Total` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `ensino_superior_cursos`
--

CREATE TABLE `ensino_superior_cursos` (
  `id` int(11) NOT NULL,
  `Categoria` varchar(255) DEFAULT NULL,
  `Indicador` varchar(255) DEFAULT NULL,
  `Ano` int(11) DEFAULT NULL,
  `valor` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `escolas_por_localizacao_2010`
--

CREATE TABLE `escolas_por_localizacao_2010` (
  `id` int(11) NOT NULL,
  `Localizacao` varchar(255) DEFAULT NULL,
  `Numero_de_escolas` int(11) DEFAULT NULL
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
  `Tipo` varchar(255) DEFAULT NULL,
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
-- Estrutura da tabela `ideb_anos_iniciais_2017_2019_2021`
--

CREATE TABLE `ideb_anos_iniciais_2017_2019_2021` (
  `id` int(11) NOT NULL,
  `Ano` int(11) DEFAULT NULL,
  `Ideb Anos Iniciais` decimal(3,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `ideb_evolucao`
--

CREATE TABLE `ideb_evolucao` (
  `id` int(11) NOT NULL,
  `ano` int(11) DEFAULT NULL,
  `ideb_5_ano` decimal(3,1) DEFAULT NULL,
  `ideb_9_ano` decimal(3,1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `matriculas_por_ciclo`
--

CREATE TABLE `matriculas_por_ciclo` (
  `id` int(11) NOT NULL,
  `Ano` int(11) NOT NULL,
  `Ciclo` varchar(255) NOT NULL,
  `Matriculas` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `matriculas_por_etapa`
--

CREATE TABLE `matriculas_por_etapa` (
  `id` int(11) NOT NULL,
  `etapa_de_ensino` varchar(255) NOT NULL,
  `quantidade_de_alunos` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `populacao_residencia_2022`
--

CREATE TABLE `populacao_residencia_2022` (
  `id` int(11) NOT NULL,
  `Ano` int(11) DEFAULT NULL,
  `População_residente` int(11) DEFAULT NULL,
  `Area_unidade_territorial` varchar(255) DEFAULT NULL,
  `Densidade` varchar(255) DEFAULT NULL
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
  `Valor` decimal(10,1) DEFAULT NULL,
  `Unidade` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `sjc_educacao`
--

CREATE TABLE `sjc_educacao` (
  `id` int(11) NOT NULL,
  `ano` int(11) DEFAULT NULL,
  `indicador` varchar(255) DEFAULT NULL,
  `valor` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura da tabela `transporte_por_regiao`
--

CREATE TABLE `transporte_por_regiao` (
  `id` int(11) NOT NULL,
  `Ano` int(11) DEFAULT NULL,
  `Regiao` varchar(255) DEFAULT NULL,
  `Automoveis` int(11) DEFAULT NULL,
  `Motos` int(11) DEFAULT NULL,
  `Caminhoes` int(11) DEFAULT NULL,
  `Total` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `dados_educacao`
--
ALTER TABLE `dados_educacao`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `densidade_demografica_sjc_2010`
--
ALTER TABLE `densidade_demografica_sjc_2010`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `docentes_por_dependencia_2010`
--
ALTER TABLE `docentes_por_dependencia_2010`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `ensino_superior_cursos`
--
ALTER TABLE `ensino_superior_cursos`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `escolas_por_localizacao_2010`
--
ALTER TABLE `escolas_por_localizacao_2010`
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
-- Índices para tabela `ideb_anos_iniciais_2017_2019_2021`
--
ALTER TABLE `ideb_anos_iniciais_2017_2019_2021`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `ideb_evolucao`
--
ALTER TABLE `ideb_evolucao`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `matriculas_por_ciclo`
--
ALTER TABLE `matriculas_por_ciclo`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `matriculas_por_etapa`
--
ALTER TABLE `matriculas_por_etapa`
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
-- Índices para tabela `sjc_educacao`
--
ALTER TABLE `sjc_educacao`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `transporte_por_regiao`
--
ALTER TABLE `transporte_por_regiao`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `dados_educacao`
--
ALTER TABLE `dados_educacao`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `densidade_demografica_sjc_2010`
--
ALTER TABLE `densidade_demografica_sjc_2010`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `docentes_por_dependencia_2010`
--
ALTER TABLE `docentes_por_dependencia_2010`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `ensino_superior_cursos`
--
ALTER TABLE `ensino_superior_cursos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `escolas_por_localizacao_2010`
--
ALTER TABLE `escolas_por_localizacao_2010`
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
-- AUTO_INCREMENT de tabela `ideb_anos_iniciais_2017_2019_2021`
--
ALTER TABLE `ideb_anos_iniciais_2017_2019_2021`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `ideb_evolucao`
--
ALTER TABLE `ideb_evolucao`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `matriculas_por_ciclo`
--
ALTER TABLE `matriculas_por_ciclo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `matriculas_por_etapa`
--
ALTER TABLE `matriculas_por_etapa`
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

--
-- AUTO_INCREMENT de tabela `sjc_educacao`
--
ALTER TABLE `sjc_educacao`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `transporte_por_regiao`
--
ALTER TABLE `transporte_por_regiao`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
