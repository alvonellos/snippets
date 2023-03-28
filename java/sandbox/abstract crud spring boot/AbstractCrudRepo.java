package com.alvonellos.uptime.repo;

import com.alvonellos.uptime.entity.BaseEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.UUID;


public abstract interface AbstractCrudRepo<E extends BaseEntity> extends JpaRepository<E, UUID> {
    // ...
}
