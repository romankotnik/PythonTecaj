drop table if exists tablice;

create table tablice (
  id integer primary key autoincrement,
  stevilka text not null,
  prekrsek text,
  casovni_zig text
);

INSERT INTO tablice (stevilka, casovni_zig, prekrsek) VALUES ('LJ-SZ-001', '2016-11-15 08:15:00', 'Hitrost: 213km/h');
INSERT INTO tablice (stevilka, casovni_zig, prekrsek) VALUES ('LJ-BORIS', '2016-11-15 08:17:00', 'Hitrost: 180km/h');
INSERT INTO tablice (stevilka, casovni_zig, prekrsek) VALUES ('LJ-ANA', '2016-11-15 08:22:00', 'Hitrost: 156km/h');
INSERT INTO tablice (stevilka, casovni_zig, prekrsek) VALUES ('LJ-KS-008', '2016-11-15 08:55:00', 'Hitrost: 140km/h');
INSERT INTO tablice (stevilka, casovni_zig, prekrsek) VALUES ('MB-JB-007', '2016-11-15 09:40:00', 'Hitrost: 191km/h');
