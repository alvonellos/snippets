package com.alvonellos.uptime.controller;

import com.alvonellos.uptime.entity.HostEntity;
import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest
class HostControllerTest extends AbstractCrudControllerTests {

    @Test
    void doFindAll() throws Exception {
        super.testGetAll();
    }

    /**
     * @return
     */
    @Override
    protected String getEndpoint() {
        return "/host";
    }

    /**
     * @return
     */
    @Override
    protected Object createEntity() {
        return new HostEntity();
    }

    /**
     * @param entity
     * @return
     */
    @Override
    protected Object updateEntity(Object entity) {
        return (HostEntity) entity;
    }
}