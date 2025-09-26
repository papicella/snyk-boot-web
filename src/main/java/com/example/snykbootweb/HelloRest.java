package com.example.snykbootweb;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping(path = "/hello")
@CrossOrigin("*")
public class HelloRest {

    @GetMapping ("/sayhello")
    public String sayHello() {
        // add return hello
        return "hello World!!!";
    }
}
