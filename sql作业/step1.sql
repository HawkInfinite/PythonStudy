CREATE TABLE `university`.`department` (		-- 保存大学的里各个系的信息
  `dept_name` VARCHAR(45) NOT NULL,				-- 系名，主码，varchar型,不能为空
  `building` VARCHAR(45),						-- 在哪栋建筑物里上课, varchar型, 可为空
  `budget` DECIMAL(10, 2) UNSIGNED NOT NULL,    -- 系预算, 无符号decimal型, 最多保留两位小数, 不为空
  PRIMARY KEY (`dept_name`));
  
CREATE TABLE `university`.`student` (			-- 保存大学中各个学生的信息
  `ID` VARCHAR(20) NOT NULL,					-- 学号, 可能出现有字母+数字的学号的就设置成varchar型了, 主码
  `name` VARCHAR(45) NOT NULL,					-- 名字, varchar型, 不能为空
  `sex` CHAR(1) NOT NULL,						-- 性别, 不能为空
  `age` INT(3) UNSIGNED NOT NULL,				-- 年龄, 无符号整形, 不能为空 
  `emotion_state` VARCHAR(15) NULL,				-- 婚姻状态, varchar型, 可为空
  `dept_name` VARCHAR(45) NULL,					-- 系名, varchar型. 可为空, 因为可能未被分配具体到哪个系, 外码. 当系名更改时, 同样进行更改, 当被删除时, 系名置空， 因为系名没了不代表学生不存在了
  PRIMARY KEY (`ID`),
  INDEX `fk_student_1_idx` (`dept_name` ASC),
  CONSTRAINT `fk_student_1`
    FOREIGN KEY (`dept_name`)
    REFERENCES `university`.`department` (`dept_name`)
    ON DELETE SET NULL
    ON UPDATE CASCADE);

CREATE TABLE `university`.`exam` (
  `student_ID` VARCHAR(20) NOT NULL,			-- 学号, 既是主码又是外码, 当学号更改时, 进行更改, 当学号被删除时, 将该行全部删除, 因为学号不见时, 即使有考试存在, 查不到具体的人, 分数也就失去了意义 
  `exam_name` VARCHAR(45) NOT NULL,				-- 考试名字, 主码, varchar型, 不能为空
  `grade` INT(3) UNSIGNED NOT NULL,				-- 考试成绩, 无符号整形, 不能为空
  PRIMARY KEY (`student_ID`, `exam_name`),
  CONSTRAINT `fk_exam_1`
    FOREIGN KEY (`student_ID`)
    REFERENCES `university`.`student` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE CASCADE);

