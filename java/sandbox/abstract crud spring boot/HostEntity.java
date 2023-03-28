package com.alvonellos.uptime.entity;

import com.alvonellos.uptime.dto.BaseDto;

import javax.persistence.Entity;
import javax.persistence.Id;
import java.util.UUID;

@Entity(name = "hosts")
public class HostEntity extends BaseEntity {

    public HostEntity() {
        super();
        this.id = UUID.randomUUID();
    }
    /**
     * @return
     */
    @Override
    public BaseDto toDto() {
        return null;
    }

    /**
     * @param entity
     * @return
     */
    @Override
    public BaseEntity toEntity(BaseDto entity) {
        return null;
    }

    /**
     * @return
     */
    @Override
    public String toString() {
        return null;
    }

    /**
     * @return
     */
    @Override
    public String toJson() {
        return null;
    }
}
