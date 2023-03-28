package com.alvonellos.uptime.service;

import com.alvonellos.uptime.dto.BaseDto;
import com.alvonellos.uptime.entity.BaseEntity;
import com.alvonellos.uptime.repo.AbstractCrudRepo;
import lombok.AllArgsConstructor;
import lombok.extern.java.Log;
import org.springframework.beans.BeanUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.UUID;
import java.util.stream.Collectors;

@Service
@Log
@AllArgsConstructor(onConstructor = @__(@Autowired))
public abstract class AbstractCrudService<T extends BaseDto, E extends BaseEntity> {

    protected final AbstractCrudRepo<E> repository;


    public List<BaseDto> getAll() {
        return repository.findAll().stream().map(BaseEntity::toDto).collect(Collectors.toList());
    }

    public Optional<BaseDto> getById(UUID id) {
        return repository.findById(id).map(BaseEntity::toDto);
    }

    public Optional<BaseDto> create(BaseDto dto) {
        E entity = (E) dto.toEntity();
        entity = repository.save(entity);
        return Optional.of(entity).map(BaseEntity::toDto);
    }


    public Optional<BaseDto> update(UUID id, T dto) {
        return repository.findById(id).map(existingEntity -> {
            BeanUtils.copyProperties(dto, existingEntity, getIgnoredProperties());
            return repository.save(existingEntity).toDto();
        });
    }

    public boolean delete(UUID id) {
        if (!repository.existsById(id)) {
            return false;
        }
        repository.deleteById(id);
        return true;
    }

    protected String[] getIgnoredProperties() {
        return new String[0];
    }
}
