package com.alvonellos.uptime.controller;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.MvcResult;

import java.util.List;
import java.util.UUID;

import static org.assertj.core.api.AssertionsForClassTypes.assertThat;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.delete;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.put;

@SpringBootTest
@AutoConfigureMockMvc
public abstract class AbstractCrudControllerTests<BaseDto> {

    @Autowired
    protected MockMvc mockMvc;

    @Autowired
    protected ObjectMapper objectMapper;

    protected abstract String getEndpoint();

    protected abstract BaseDto createEntity();

    protected abstract BaseDto updateEntity(BaseDto entity);

    @Test
    void testGetAll() throws Exception {
        // Given
        BaseDto entity1 = createEntity();
        BaseDto entity2 = createEntity();
        mockMvc.perform(get(getEndpoint()).contentType(MediaType.APPLICATION_JSON).content(asJsonString(entity1)));
        mockMvc.perform(get(getEndpoint()).contentType(MediaType.APPLICATION_JSON).content(asJsonString(entity2)));

        // When
        MvcResult result = mockMvc.perform(get(getEndpoint()).contentType(MediaType.APPLICATION_JSON)).andReturn();

        // Then
        int statusCode = result.getResponse().getStatus();
        assertThat(statusCode).isEqualTo(HttpStatus.OK.value());
        List<BaseDto> entities = objectMapper.readValue(result.getResponse().getContentAsString(),
                objectMapper.getTypeFactory().constructCollectionType(List.class, entity1.getClass()));
        assert(entities.size() == 2);
    }

    @Test
    void testGetById() throws Exception {
        // Given
        BaseDto entity = createEntity();
        MvcResult createResult = mockMvc.perform(post(getEndpoint()).contentType(MediaType.APPLICATION_JSON)
                .content(entity.toString())).andReturn();
        UUID id = objectMapper.readValue(createResult.getResponse().getContentAsString(), UUID.class);

        // When
        MvcResult getResult = mockMvc.perform(get(getEndpoint() + "/" + id).contentType(MediaType.APPLICATION_JSON))
                .andReturn();

        // Then
        int statusCode = getResult.getResponse().getStatus();
        assertThat(statusCode).isEqualTo(HttpStatus.OK.value());
        BaseDto returnedEntity = (BaseDto) objectMapper.readValue(getResult.getResponse().getContentAsString(), entity.getClass());
        assertThat(returnedEntity).isEqualTo(entity);
    }

    @Test
    void testCreate() throws Exception {
        // Given
        BaseDto entity = createEntity();

        // When
        MvcResult result = mockMvc.perform(post(getEndpoint()).contentType(MediaType.APPLICATION_JSON)
                .content(asJsonString(entity))).andReturn();

        // Then
        int statusCode = result.getResponse().getStatus();
        assertThat(statusCode).isEqualTo(HttpStatus.CREATED.value());
        BaseDto returnedEntity = (BaseDto) objectMapper.readValue(result.getResponse().getContentAsString(), entity.getClass());
        assert(returnedEntity.equals(entity));
    }

    @Test
    void testUpdate() throws Exception {
        // Given
        BaseDto entity = createEntity();
        MvcResult createResult = mockMvc.perform(put(getEndpoint()).contentType(MediaType.APPLICATION_JSON)
                .content(asJsonString(entity))).andReturn();
        UUID id = objectMapper.readValue(createResult.getResponse().getContentAsString(), UUID.class);
        BaseDto updatedEntity = updateEntity(entity);

        // When
        MvcResult updateResult = mockMvc.perform(put(getEndpoint() + "/" + id).contentType(MediaType.APPLICATION_JSON)
                .content(asJsonString(updatedEntity))).andReturn();

        // Then
        int statusCode = updateResult.getResponse().getStatus();
        assertThat(statusCode).isEqualTo(HttpStatus.OK.value());
        BaseDto returnedEntity = (BaseDto) objectMapper.readValue(updateResult.getResponse().getContentAsString(), entity.getClass());
        assertThat(returnedEntity).isEqualTo(updatedEntity);
    }

    @Test
    void testDelete() throws Exception {
        // Given
        BaseDto entity = createEntity();
        MvcResult createResult = mockMvc.perform(delete(getEndpoint()).contentType(MediaType.APPLICATION_JSON)
                .content(asJsonString(entity))).andReturn();
        UUID id = objectMapper.readValue(createResult.getResponse().getContentAsString(), UUID.class);

        // When
        MvcResult deleteResult = mockMvc.perform(delete(getEndpoint() + "/" + id).contentType(MediaType.APPLICATION_JSON))
                .andReturn();

        // Then
        int statusCode = deleteResult.getResponse().getStatus();
        assertThat(statusCode).isEqualTo(HttpStatus.NO_CONTENT.value());

        MvcResult getResult = mockMvc.perform(get(getEndpoint() + "/" + id).contentType(MediaType.APPLICATION_JSON))
                .andReturn();
        int getStatusCode = getResult.getResponse().getStatus();
        assertThat(getStatusCode).isEqualTo(HttpStatus.NOT_FOUND.value());
    }

    protected byte[] asJsonString(BaseDto entity1) {
        try {
            return objectMapper.writeValueAsBytes(entity1);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}