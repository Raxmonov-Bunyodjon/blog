from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    #bu funksiya ishlashi pastdagi funksiya bilan bir xil farqi argumentlarida bor
    # def has_permission(self, request, view):
    #     if request.user.is_authenticated:
    #         return True
    #     else: return False
#tizimga kirmagan bo`lsa ham postni ko'radi
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
    

