import 'package:flutter/material.dart';
import 'package:todolist/pages/todolist.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  //const MyApp({ Key? key }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    // เรื่องใช้หลายหน้า ใช้ home
    return MaterialApp( 
      debugShowCheckedModeBanner: false, // เอา debug ออก
      title: "Todolist App",
      home: Todolist(),
    );
  }
}