package com.example.snykbootweb.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @GetMapping ("/")
    public String sayHello () {
        return "hello world web app for snyk springboot jdbc demo";
    }
}
