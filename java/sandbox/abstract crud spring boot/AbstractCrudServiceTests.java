package com.alvonellos.uptime.service;

import com.alvonellos.uptime.dto.BaseDto;
import com.alvonellos.uptime.entity.BaseEntity;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest;
import org.springframework.boot.test.autoconfigure.orm.jpa.TestEntityManager;

import java.util.List;
import java.util.Optional;
import java.util.UUID;

import static org.assertj.core.api.AssertionsForClassTypes.assertThat;
import static org.mockito.ArgumentMatchers.any;

@DataJpaTest
public abstract class AbstractCrudServiceTests {

    @Autowired
    protected TestEntityManager entityManager;

    protected AbstractCrudService<BaseDto, BaseEntity> service;

    protected abstract AbstractCrudService<BaseDto, BaseEntity> getService();

    protected abstract BaseEntity createEntity();

    @BeforeEach
    void setUp() {
        service = getService();
    }

    @Test
    void testGetAll() {
        // Given
        BaseEntity entity1 = createEntity();
        BaseEntity entity2 = createEntity();
        entityManager.persist(entity1);
        entityManager.persist(entity2);

        // When
        List<BaseDto> result = service.getAll();

        // Then
        assertThat(result.size()).isEqualTo(2);
    }

    @Test
    void testGetById() {
        // Given
        BaseEntity entity = createEntity();
        entityManager.persist(entity);

        // When
        Optional<BaseDto> result = (Optional<BaseDto>) service.getById(any());

        // Then
        assertThat(result).isNotNull();
    }

    @Test
    void testCreate() {
        // Given
        BaseDto dto = createEntity().toDto();

        // When
        Optional<BaseDto> result = service.create(dto);

        // Then
        assertThat(result).isNotNull();
    }

    @Test
    void testUpdate() {
        // Given
        BaseEntity entity = createEntity();
        entityManager.persist(entity);
        BaseDto updatedEntity = createEntity().toDto();

        // When
        Optional<BaseDto> result = service.update(entity.getId(), updatedEntity);

        // Then
        assertThat(result).isPresent();
        assertThat(result.get()).isEqualTo(updatedEntity);
    }

    @Test
    void testDelete() {
        // Given
        BaseEntity entity = createEntity();
        entityManager.persist(entity);

        // When
        boolean result = service.delete(entity.getId());

        // Then
        assertThat(result).isTrue();
        assertThat(entityManager.find(entity.getClass(), 1L)).isNull();
    }
}

