package com.alvonellos.uptime.entity;

import com.alvonellos.uptime.dto.BaseDto;
import com.fasterxml.jackson.annotation.JsonGetter;
import com.fasterxml.jackson.annotation.JsonInclude;

import javax.annotation.PostConstruct;
import javax.persistence.*;
import java.util.Date;
import java.util.UUID;

@JsonInclude(value = JsonInclude.Include.NON_NULL)
@MappedSuperclass
public abstract class BaseEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    @Column(name = "id", nullable = false)
    protected UUID id;

    @Temporal(TemporalType.TIMESTAMP)
    @Column(name = "created_at", nullable = false)
    protected Date createdAt;

    @Temporal(TemporalType.TIMESTAMP)
    @Column(name = "updated_at", nullable = false)
    protected Date updatedAt;

    @PostConstruct
    public void init() {
        this.createdAt = new Date();
        this.updatedAt = new Date();
    }

    @PostUpdate
    public void update() {
        this.updatedAt = new Date();
    }


    public UUID getId() {
        return id;
    }

    public void setId(UUID id) {
        this.id = id;
    }

    public Date getCreatedAt() {
        return createdAt;
    }

    public Date getUpdatedAt() {
        return updatedAt;
    }

    public abstract BaseDto toDto();

    public abstract BaseEntity toEntity(BaseDto entity);

    public abstract String toString();

    @JsonGetter
    public abstract String toJson();
}
