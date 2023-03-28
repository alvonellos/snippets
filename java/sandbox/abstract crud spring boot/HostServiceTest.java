package com.alvonellos.uptime.service;

import com.alvonellos.uptime.dto.BaseDto;
import com.alvonellos.uptime.entity.BaseEntity;

import static org.junit.jupiter.api.Assertions.*;

class HostServiceTest extends AbstractCrudServiceTests {

    /**
     * @return
     */
    @Override
    protected AbstractCrudService<BaseDto, BaseEntity> getService() {
        return null;
    }

    /**
     * @return
     */
    @Override
    protected BaseEntity createEntity() {
        return null;
    }
}