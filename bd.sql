DROP TABLE IF EXISTS `Votes`;
		
CREATE TABLE `Votes` (
  `id` INTEGER NULL AUTO_INCREMENT DEFAULT NULL,
  `votacion_id` INTEGER NOT NULL,
  `vote` MEDIUMTEXT NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO `Votes` (`votacion_id`,`vote`) VALUES (1,'vote1')