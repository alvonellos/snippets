package com.alvonellos.uptime.controller;

import com.alvonellos.uptime.dto.BaseDto;
import com.alvonellos.uptime.entity.BaseEntity;
import com.alvonellos.uptime.service.AbstractCrudService;
import lombok.AllArgsConstructor;
import lombok.extern.java.Log;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.support.ServletUriComponentsBuilder;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

@RestController
@AllArgsConstructor(onConstructor = @__(@Autowired))
@Log
public abstract class AbstractCrudController<T extends BaseDto, E extends BaseEntity> {

    protected final AbstractCrudService<T, E> abstractCrudService;

    protected String basePath;

    public AbstractCrudController(AbstractCrudService<T, E> abstractCrudService) {
        this.abstractCrudService = abstractCrudService;
    }

    @GetMapping
    public ResponseEntity<List<BaseDto>> getAll() {
        return ResponseEntity.ok(abstractCrudService.getAll());
    }

    @GetMapping("/{id}")
    public ResponseEntity<BaseDto> getById(@PathVariable UUID id) {
        return abstractCrudService.getById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    @PostMapping
    public ResponseEntity<BaseDto> create(@RequestBody T entity) {

        Optional<BaseDto> createdEntity = abstractCrudService.create(entity);
        return ResponseEntity.created(
                        ServletUriComponentsBuilder.fromCurrentRequest()
                                .path("/{id}")
                                .buildAndExpand(createdEntity.get().getId())
                                .toUri())
                .body(createdEntity.get());
    }

    @PutMapping("/{id}")
    public ResponseEntity<BaseDto> update(@PathVariable UUID id, @RequestBody T entity) {
      return ResponseEntity
              .accepted()
              .body(abstractCrudService.update(id, entity).get());
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable UUID id) {
        abstractCrudService.delete(id);
        return ResponseEntity.noContent().build();
    }
}

