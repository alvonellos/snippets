package com.alvonellos.uptime.dto;

import com.alvonellos.uptime.entity.BaseEntity;
import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import lombok.Data;

import java.util.UUID;

@JsonInclude(value = JsonInclude.Include.NON_NULL)
@Data
public abstract class BaseDto {
    protected UUID id;

    public UUID getId() {
        return id;
    }

    public void setId(UUID id) {
        this.id = id;
    }

    public abstract BaseEntity toEntity();

    public abstract BaseDto fromEntity(BaseEntity entity);

    public abstract String toString();

    @JsonGetter
    public abstract String toJson();
}
