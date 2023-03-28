package com.alvonellos.uptime.controller;

import com.alvonellos.uptime.dto.BaseDto;
import com.alvonellos.uptime.dto.HostDto;
import com.alvonellos.uptime.entity.HostEntity;
import com.alvonellos.uptime.service.AbstractCrudService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.List;

@RequestMapping("/host")
public class HostController extends AbstractCrudController <HostDto, HostEntity>{
    public HostController(AbstractCrudService<HostDto, HostEntity> abstractCrudService) {
        super(abstractCrudService);
    }

    @Override
    @GetMapping
    public ResponseEntity<List<BaseDto>> getAll() {
        super.create(new HostDto());
        return super.getAll();
    }
}
