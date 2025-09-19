package com.example.snykbootweb.jdbc;

import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping(path = "/customer")
public class CustomerRest {

    CustomerService customerService;

    public CustomerRest(CustomerService customerService) {
        this.customerService = customerService;
    }

    @GetMapping ("/count")
    public int getCount() {
        return customerService.countCustomers();
    }

    @GetMapping(produces = "application/json", path = "/all")
    public List<Customer> getAllCustomers() {
        return customerService.getAll();
    }

    @GetMapping(produces = "application/json", path = "/all/{lastName}")
    public List<Customer> getAllCustomersByLastName(@PathVariable String lastName) {
        return customerService.getAllByLastName(lastName);
    }

    @GetMapping(produces = "application/json", path = "/all/{firstName}")
    public List<Customer> getAllCustomersByFirstName(@PathVariable String firstName) {
        List<Customer> customers = customerService.jdbcTemplate.query(
                "SELECT id, first_name, last_name FROM customers WHERE first_name = '" + firstName + "'",
                (rs, rowNum) -> new Customer((int) rs.getLong("id"),
                        rs.getString("first_name"),
                        rs.getString("last_name")));

        return customers;
    }

    /*
    @GetMapping(produces = "application/json", path = "/all/withfix/{lastName}")
    public List<Customer> getAllCustomersByLastNameFixed(@PathVariable String lastName) {
        return customerService.getAllByLastNameFixed(lastName);
    }


    /* TO REMOVE
    @GetMapping(produces = "application/json", path = "/all/withfix/{lastName}")
    public List<Customer> getAllCustomersByLastNameFixed(@PathVariable String lastName) {
        return customerService.getAllByLastNameFixed(lastName);
    }
    */
}
