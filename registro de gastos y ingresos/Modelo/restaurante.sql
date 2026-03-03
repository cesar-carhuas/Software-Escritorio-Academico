create database restaurante;
use restaurante;

create table empleado(
	idempleado int primary key auto_increment,
    nombreEmp varchar(50) not null,
    apellidoEmp varchar(50) not null,
    usuario varchar(50) not null,
    contraseña varchar(50) not null,
    telefono varchar(15) not null,
    correo varchar(100) not null
);

insert into empleado values 
('1','cesar daniel','carhuas aldana','CesarCarhuas','123456','934110870','cesar@gmail.com');
select * from empleado;

create table historial(
	idingreso INT primary key auto_increment,
    fecha date not null,
    tipo varchar(50) not null,
    nombre varchar(50) not null,
    salida double not null,
    entrada double not null
);

insert into historial values 
('1','2024/02/09','PASAJE','Metropolitano',5.00,'0'),
('2','2024/02/09','TRABAJO','Sueldo','0',1025);
select * from historial;


