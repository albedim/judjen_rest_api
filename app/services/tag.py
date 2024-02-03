from app.model.repository.repo import Repository
from app.model.entity.tag import Tag
from app.model.repository.tag import TagRepository
from app.utils.utils import createSuccessResponse


class TagService(Repository):

    @classmethod
    def getTags(cls):
        tags = TagRepository.getTags()
        res = []
        for tag in tags:
            res.append(tag.toJSON())
        return createSuccessResponse(res)