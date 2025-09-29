package com.example.snykbootweb.controller;

import com.example.snykbootweb.DatabaseService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@CrossOrigin("*")
@RestController
public class HelloController {

    @Autowired
    DatabaseService databaseService;

    @GetMapping ("/")
    public String sayHello () {
        String password = databaseService.getPassword();
        return "hello world web app for snyk springboot jdbc demo, password = " + password;
    }
}
